# -*- coding: utf-8 -*-
import xml.dom.minidom
import sys
import MysqlHelper


reload(sys)
sys.setdefaultencoding("utf-8")


class LoadMetadata(object):
    def __init__(self, dbCursor, configFilePath, tableName, conn):  # CRJ_CCRJZJRYXX
        self.con = conn
        self.cursor = dbCursor
        self.configFilePath = configFilePath
        self.tableName = tableName

        mappingRoot = self.__getConf("mapping")  # xml中的mapping所有xml信息
        typeRoot = self.__getConf("type-mapping")  # xml中的type所有xml信息

        if self.__createNewTable(self.tableName, mappingRoot, typeRoot) == -1:
            return
        self.__loadNewRecordsFromMetaData(self.tableName, '2', mappingRoot)
        self.__printMergeData('mysql_' + self.tableName, '2')  # 打印声称数据 参数（新表名，数据库连接句柄，打印数量）

    def __getConf(self, nodeName):
        domTree = xml.dom.minidom.parse(self.configFilePath)
        collection = domTree.documentElement
        root = collection.getElementsByTagName(nodeName)
        return root[0]

    def __createNewTable(self, tableName, mappingRoot, typeRoot):
        if self.cursor is not None:
            getExistTablesSql = 'show tables'
            self.cursor.execute(getExistTablesSql)
            tableToCreateAlreadyExist = False

            for row in self.cursor.fetchall():
                if row[0] == 'mysql_' + tableName:
                    tableToCreateAlreadyExist = True

            if tableToCreateAlreadyExist:
                print "Table '" + 'mysql_' + tableName + "' already exists."
                return -1

            sql = "select innerId,fieldName,fieldDescription,fieldType,length from tables where tableName='" + tableName + "'"
            self.cursor.execute(sql)
            sql = "CREATE TABLE IF NOT EXISTS mysql_" + tableName + "("
            primaryKey = ""
            for row in self.cursor.fetchall():
                new_field = self.__getNodeValueByAttribute(row[1], mappingRoot)
                new_fieldType = self.__getNodeValueByAttribute(row[3], typeRoot)
                new_comment = row[2]
                if row[4] == "":
                    new_length = ""
                else:
                    new_length = "(" + row[4] + ")"
                if row[0] == 1:
                    primaryKey = new_field
                sql += "`" + new_field + "` " + new_fieldType + new_length
                if new_fieldType == "VARCHAR" or new_fieldType == "CHAR":
                    sql += " CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT '" + new_comment + "',"
                else:
                    sql += " NOT NULL COMMENT '" + new_comment + "',"

            sql += "PRIMARY KEY (`" + primaryKey + "`))ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci "
            self.cursor.execute(sql)
            return 0


    def __loadNewRecordsFromMetaData(self, tableName, num, mappingRoot):
        if self.cursor is not None:
            columnsArray = self.__getTableColsArray(tableName)

            sql_read = "select * from " + tableName + " limit 0," + num
            self.cursor.execute(sql_read)

            for row_read in self.cursor.fetchall():  # 遍历查找的结果
                i = 0
                sql_merge = "insert into mysql_" + tableName + " SET "
                for eachUnit in row_read:  # 读取每个单元值
                    new_field = self.__getNodeValueByAttribute(columnsArray[i], mappingRoot)
                    sql_merge += new_field + "='" + str(eachUnit) + "',"
                    i += 1
                sql_merge = sql_merge.strip().lstrip().rstrip(',')
                self.cursor.execute(sql_merge)

            return

    def __getNodeValueByAttribute(self, attributeName, mappingNode):
        node = mappingNode.getElementsByTagName(attributeName)[0].childNodes[0].nodeValue
        return node if node else ''


    # 获取表的字段数组
    def __getTableColsArray(self, tableName):
        if self.cursor is not None:
            columnsArray = []
            sql_cols = "SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE table_name ='" + tableName + "'"
            self.cursor.execute(sql_cols)
            row_cols = self.cursor.fetchall()
            for row_col in row_cols:
                columnsArray.append(row_col[0])
            return columnsArray

    def __printMergeData(self, tableName, num):
        if self.cursor is not None:
            columnsArray = self.__getTableColsArray(tableName)
            sql = "SELECT * FROM " + tableName + " limit 0," + num
            info = "{\nstorage:HBase\n"
            self.cursor.execute(sql)
            for row in self.cursor.fetchall():
                i = 0
                info += "\trecords:{\n"
                for eachUnit in row:
                    # print eachUnit, columnsArray[i]
                    info += "\t\t" + columnsArray[i] + " : " + str(eachUnit) + "\n"
                    i += 1
                info += "\t}\n}"
            print info


if __name__ == '__main__':
    conn = MysqlHelper.DB("localhost", 3306, "root", "", "metadata")
    LoadMetadata(conn.getCursor(), './config/mapping.conf', 'CRJ_CCRJZJRYXX', conn)