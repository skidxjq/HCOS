# coding=utf-8
import MySQLdb


class DB():
    conn = None

    def __init__(self, DB_HOST, DB_PORT, DB_USER, DB_PWD, DB_NAME):
        self.DB_HOST = DB_HOST
        self.DB_PORT = DB_PORT
        self.DB_USER = DB_USER
        self.DB_PWD = DB_PWD
        self.DB_NAME = DB_NAME
        self.conn = self.__getConnection()

    def __del__(self):
        if self.conn is not None:
            self.conn.close()

    def __getConnection(self):
        conn = None
        try:
            conn = MySQLdb.Connect(
                host=self.DB_HOST,  # 设置MYSQL地址
                port=self.DB_PORT,  # 设置端口号
                user=self.DB_USER,  # 设置用户名
                passwd=self.DB_PWD,  # 设置密码
                db=self.DB_NAME,  # 数据库名
                charset='utf8'  # 设置编码
            )
        except MySQLdb.Error, e:
            print "MYSQL ERROR %d: %s" % (e.args[0], e.args[1])
        return conn

    def getCursor(self):
        if self.conn is not None:
            return self.conn.cursor()
        return None

    def query(self, sqlString):
        if self.conn is not None:
            cursor = self.conn.cursor()
            cursor.execute(sqlString)
            returnData = cursor.fetchall()
            cursor.close()
            return returnData

