# coding=utf-8
# This is the Command Line Interface(CLI) of the project.
import CheckUserPassword
import MetaDataIndustry
import MysqlHelper
import sys
import CONSTANT
import readInXml

reload(sys)
sys.setdefaultencoding("utf-8")


class Shell(object):
    isLogIn = False

    def __init__(self, configFilePath):
        self.configFilePath = configFilePath
        self.dbHelper = None
        # self.dbHelper = MysqlHelper.DB("localhost", 3306, "root", "", "metadata")
        self.dbHelper = MysqlHelper.DB(readInXml.getElement(self.configFilePath, 'DatabaseConfig', 'host'),
                                       int(readInXml.getElement(self.configFilePath, 'DatabaseConfig', 'port')),
                                       readInXml.getElement(self.configFilePath, 'DatabaseConfig', 'userName'),
                                       "",
                                       readInXml.getElement(self.configFilePath, 'DatabaseConfig', 'dbName'))

    def execute(self):
        directive = ''
        print CONSTANT.greeting
        while not self.isLogIn:
            self.__login__()
        while self.isLogIn and directive != 'quit':
            directive = raw_input('HCOS>')

            if directive == 'metadata industry -a' or directive == 'metadata industry -all':
                metaDataTypeArray = MetaDataIndustry.getAllMetadataIndustryType(
                    readInXml.getElement(self.configFilePath, 'metadataIndustry', 'filePath'))
                for index in range(len(metaDataTypeArray)):
                    print str(index + 1) + '. ' + metaDataTypeArray[index]

            elif directive == 'metadata get police':
                self.__metaDataGetPolice()

            elif directive == 'metadata get police/people' \
                    or directive == 'metadata get police/items' \
                    or directive == 'metadata get police/events' \
                    or directive == 'metadata get police/orgs' \
                    or directive == 'metadata get police/locations':
                self.__metaDataGetPoliceType(directive)

            elif directive.startswith('metadata get police/people/') \
                    or directive.startswith('metadata get police/items/') \
                    or directive.startswith('metadata get police/events/') \
                    or directive.startswith('metadata get police/orgs/') \
                    or directive.startswith('metadata get police/locations/'):
                self.__metaDataGetPoliceTypeTable(directive)

            elif directive == 'metadata load police/people/sdryxx -conf mapping.conf ':
                print 'metadata load police/people/sdryxx -conf mapping.conf '

            elif directive == '':
                pass

            else:
                print 'invalid command, please check and retry'

    def __metaDataGetPolice(self):
        if self.dbHelper.conn is not None:
            data = self.dbHelper.query('select distinct category from tables')
            for index in range(len(data)):
                print str(index + 1) + '. ' + data[index][0]

    def __metaDataGetPoliceType(self, directive):
        if self.dbHelper.conn is not None:
            data = self.dbHelper.query(
                "select tableDescription, tableName from tables  where category='" + CONSTANT.categoryDict[
                    directive[len('metadata get police/'):]] + "' group by tableName")
            for index in range(len(data)):
                print '%d.%s (%s)' % (index + 1, data[index][1].rstrip('\r\n'), data[index][0].rstrip('\r\n'))
        else:
            print 'Error with mysql, please check and retry'

    def __metaDataGetPoliceTypeTable(self, directive):
        directiveInArray = directive.split('/', 2)
        if directiveInArray[1] in CONSTANT.categoryDict.keys():
            if self.dbHelper.conn is not None:
                data = self.dbHelper.query(
                    "select innerId,fieldName,fieldDescription  from tables where tableName='" +
                    directiveInArray[2] + "' " + "and category='" + CONSTANT.categoryDict[
                        directiveInArray[1]] + "'")
                if len(data) == 0:
                    print 'no table named:' + directive[len('metadata get police/people/'):]
                else:
                    for index in range(len(data)):
                        if str(data[index][0]) == '1':
                            print '%s %s %s is primary key!' % (str(data[index][0]),
                                                                str(data[index][1]),
                                                                str(data[index][2]))
                        else:
                            print '%s %s %s' % (str(data[index][0]),
                                                str(data[index][1]),
                                                str(data[index][2]))
            else:
                print 'Error with mysql, please check and retry'
        else:
            print 'no table named:' + directiveInArray[2]

    def __login__(self):
        print "input 'login' command to login and go on."
        directive = raw_input('HCOS>')  # get the directive from user
        if directive == 'login':
            userName = raw_input('please input user name:')
            passWord = raw_input('please input password:')
            if CheckUserPassword.check(readInXml.getElement(self.configFilePath, 'usersConfig', 'userConfigFilePath'),
                                       userName, passWord):
                self.isLogIn = True
                print 'login successfully'
            else:
                self.isLogIn = False
                print 'login failed, please check your input and try again!'


if __name__ == '__main__':
    shell = Shell('./config/config.xml')
    shell.execute()