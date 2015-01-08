# -*- coding: utf-8 -*-
import xml.dom.minidom
import MySQLdb

def getConf(configFilePath,nodeName):

    domTree = xml.dom.minidom.parse(configFilePath)
    collection = domTree.documentElement
    print collection
    root = collection.getElementsByTagName(nodeName)
    return root[0]

#根据属性名获取属性值
def getNodeValueByAttribute(attributeName,mappingNode):
  # root.getElementsByTagName('SFZMHM')[0].childNodes[0].data
  #   print mappingNode.nodeName
    node=mappingNode.getElementsByTagName(attributeName)[0].childNodes[0].nodeValue
    return node if node else ''

def test(mappingNode):
  # root.getElementsByTagName('SFZMHM')[0].childNodes[0].data
   # print '++++++++++++++++++++++++'
    print mappingNode.getElementsByTagName('XZZ')[0].childNodes[0].nodeValue


#连接数据库
def connectDb():
    conn=MySQLdb.connect(host="localhost",user="root",passwd="",db="metadata",charset="utf8")
    cursor=conn.cursor()
    return cursor


####生成新表            默认只能生成一个新表
def mergeNewTable(tableName,cursor,mappingRoot,typeRoot):
    sql="select innerId,fieldName,fieldDescription,fieldType,length from tables where tableName='"+tableName+"'"
    # print sql
    query=cursor.execute(sql)
   # print test(mappingRoot)
    sql="CREATE TABLE IF NOT EXISTS mysql_"+tableName+"("
    primaryKey=""
    for row in cursor.fetchall():

        new_field       =   getNodeValueByAttribute(row[1],mappingRoot)
        new_fieldType   =   getNodeValueByAttribute(row[3],typeRoot)
        new_comment     =   row[2]
        if row[4]=="":
            new_length=""
        else:
            new_length="("+row[4]+")"
        if row[0]==1:primaryKey=new_field
        sql+="`"+new_field+"` "+new_fieldType+new_length
        if new_fieldType=="VARCHAR" or new_fieldType =="CHAR":
            sql+=" CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL COMMENT '"+new_comment+"',"
        else:
            sql+=" NOT NULL COMMENT '"+new_comment+"',"

    sql+="PRIMARY KEY (`"+primaryKey+"`))ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci "
    # print sql
    query=cursor.execute(sql)
    return 1
    # print primaryKey
#导入新的数据
def importRecordsFromMetaData(tableName,num):
    return



def main():
    cursor=connectDb()
    filePath="C:/mapping.conf"
    mappingRoot	=	getConf(filePath,"mapping")    #xml中的mapping所有xml信息
    typeRoot	=	getConf(filePath,"type-mapping")    #xml中的type所有xml信息
    mergeNewTable('CRJ_CCRJZJRYXX',cursor,mappingRoot,typeRoot)

    # getNodeValueByAttribute('XM',mappingRoot)



if __name__=='__main__':
    main()
