# coding=utf-8
import MySQLdb


class DB():
    def __init__(self, DB_HOST, DB_PORT, DB_USER, DB_PWD, DB_NAME):
        self.DB_HOST = DB_HOST
        self.DB_PORT = DB_PORT
        self.DB_USER = DB_USER
        self.DB_PWD = DB_PWD
        self.DB_NAME = DB_NAME
        self.conn = self.__getConnection()

    def __del__(self):
        self.conn.close()

    def __getConnection(self):
        return MySQLdb.Connect(
            host=self.DB_HOST,  # 设置MYSQL地址
            port=self.DB_PORT,  # 设置端口号
            user=self.DB_USER,  # 设置用户名
            passwd=self.DB_PWD,  # 设置密码
            db=self.DB_NAME,  # 数据库名
            charset='utf8'  # 设置编码
        )

    def query(self, sqlString):
        cursor = self.conn.cursor()
        cursor.execute(sqlString)
        returnData = cursor.fetchall()
        cursor.close()
        return returnData

        # def update(self, sqlString):
        # cursor = self.conn.cursor()
        # cursor.execute(sqlString)
        # self.conn.commit()
        # cursor.close()
        #     self.conn.close()


        # if __name__ == '__main__':
        #     dbHelper = DB("localhost", 3306, "root", "", "metadata")
        #     data = dbHelper.query("select tableDescription, tableName from tables  where category='人员要素' group by tableName")
        #     for index in range(len(data)):
        #         print '%s %s' % (data[index][1].rstrip('\r\n'), data[index][0].rstrip('\r\n'))