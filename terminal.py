# coding=utf-8
# This is the Command Line Interface(CLI) of the project.
import CheckUserPassword
import MetaDataIndustry
import MysqlHelper


class Shell(object):
    # todo make it False
    isLogIn = True

    def __init__(self):
        self.dbHelper = None
        self.dbHelper = MysqlHelper.DB("localhost", 3306, "root", "", "metadata")

    def execute(self):
        directive = ''
        print '=' * 40 + '\n\t welcome\n' + '=' * 40
        while not self.isLogIn:
            self.__login__()
        while self.isLogIn and directive != 'quit':
            directive = raw_input('HCOS>')

            if directive == 'metadata industry -a' or directive == 'metadata industry -all':
                metaDataTypeArray = MetaDataIndustry.getAllMetadataIndustryType('metadataIndustry.xml')
                for index in range(len(metaDataTypeArray)):
                    print str(index + 1) + '. ' + metaDataTypeArray[index]

            elif directive == 'metadata get police':
                if self.dbHelper is not None:
                    data = self.dbHelper.query('select distinct category from tables')
                    for index in range(len(data)):
                        print str(index + 1) + '. ' + data[index][0]

            elif directive == 'metadata get police/people':
                if self.dbHelper is not None:
                    data = self.dbHelper.query(
                        "select tableDescription, tableName from tables  where category='人员要素' group by tableName")
                    for index in range(len(data)):
                        print '%s %s' % (data[index][1].rstrip('\r\n'), data[index][0].rstrip('\r\n'))

            elif directive == 'metadata get police/items':
                if self.dbHelper is not None:
                    data = self.dbHelper.query(
                        "select tableDescription, tableName from tables  where category='物品要素' group by tableName")
                    for index in range(len(data)):
                        print '%s %s' % (data[index][1].rstrip('\r\n'), data[index][0].rstrip('\r\n'))

            elif directive == 'metadata get police/events':
                if self.dbHelper is not None:
                    data = self.dbHelper.query(
                        "select tableDescription, tableName from tables  where category='案(事)件要素' group by tableName")
                    for index in range(len(data)):
                        print '%s %s' % (data[index][1].rstrip('\r\n'), data[index][0].rstrip('\r\n'))

            elif directive == 'metadata get police/orgs':
                if self.dbHelper is not None:
                    data = self.dbHelper.query(
                        "select tableDescription, tableName from tables  where category='机构要素' group by tableName")
                    for index in range(len(data)):
                        print '%s %s' % (data[index][1].rstrip('\r\n'), data[index][0].rstrip('\r\n'))

            elif directive == 'metadata get police/locations':
                if self.dbHelper is not None:
                    data = self.dbHelper.query(
                        "select tableDescription, tableName from tables  where category='地点要素' group by tableName")
                    for index in range(len(data)):
                        print '%s %s' % (data[index][1].rstrip('\r\n'), data[index][0].rstrip('\r\n'))

            elif directive.startswith('metadata get police/people/'):
                if self.dbHelper is not None:
                    data = self.dbHelper.query(
                        "select innerId,fieldName,fieldDecription  from tables where tableName='" + directive[len(
                            'metadata get police/people/'):] + "'")
                    for index in range(len(data)):
                        if str(data[index][0]) == '1':
                            print '%s %s %s is primary key!' % (str(data[index][0]).rstrip('\r\n'),
                                                                str(data[index][1]).rstrip('\r\n'),
                                                                str(data[index][2]).rstrip('\r\n'))
                        else:
                            print '%s %s %s' % (str(data[index][0]).rstrip('\r\n'),
                                                str(data[index][1]).rstrip('\r\n'),
                                                str(data[index][2]).rstrip('\r\n'))

            elif directive.startswith('metadata get police/items/'):
                if self.dbHelper is not None:
                    data = self.dbHelper.query(
                        "select innerId,fieldName,fieldDecription  from tables where tableName='" + directive[len(
                            'metadata get police/items/'):] + "'")
                    for index in range(len(data)):
                        if str(data[index][0]) == '1':
                            print '%s %s %s is primary key!' % (str(data[index][0]).rstrip('\r\n'),
                                                                str(data[index][1]).rstrip('\r\n'),
                                                                str(data[index][2]).rstrip('\r\n'))
                        else:
                            print '%s %s %s' % (str(data[index][0]).rstrip('\r\n'),
                                                str(data[index][1]).rstrip('\r\n'),
                                                str(data[index][2]).rstrip('\r\n'))

            elif directive.startswith('metadata get police/events/'):
                if self.dbHelper is not None:
                    data = self.dbHelper.query(
                        "select innerId,fieldName,fieldDecription  from tables where tableName='" + directive[len(
                            'metadata get police/events/'):] + "'")
                    for index in range(len(data)):
                        if str(data[index][0]) == '1':
                            print '%s %s %s is primary key!' % (str(data[index][0]).rstrip('\r\n'),
                                                                str(data[index][1]).rstrip('\r\n'),
                                                                str(data[index][2]).rstrip('\r\n'))
                        else:
                            print '%s %s %s' % (str(data[index][0]).rstrip('\r\n'),
                                                str(data[index][1]).rstrip('\r\n'),
                                                str(data[index][2]).rstrip('\r\n'))

            elif directive.startswith('metadata get police/orgs/'):
                if self.dbHelper is not None:
                    data = self.dbHelper.query(
                        "select innerId,fieldName,fieldDecription  from tables where tableName='" + directive[len(
                            'metadata get police/orgs/'):] + "'")
                    for index in range(len(data)):
                        if str(data[index][0]) == '1':
                            print '%s %s %s is primary key!' % (str(data[index][0]).rstrip('\r\n'),
                                                                str(data[index][1]).rstrip('\r\n'),
                                                                str(data[index][2]).rstrip('\r\n'))
                        else:
                            print '%s %s %s' % (str(data[index][0]).rstrip('\r\n'),
                                                str(data[index][1]).rstrip('\r\n'),
                                                str(data[index][2]).rstrip('\r\n'))

            elif directive.startswith('metadata get police/locations/'):
                if self.dbHelper is not None:
                    data = self.dbHelper.query(
                        "select innerId,fieldName,fieldDecription  from tables where tableName='" + directive[len(
                            'metadata get police/locations/'):] + "'")
                    for index in range(len(data)):
                        if str(data[index][0]) == '1':
                            print '%s %s %s is primary key!' % (str(data[index][0]).rstrip('\r\n'),
                                                                str(data[index][1]).rstrip('\r\n'),
                                                                str(data[index][2]).rstrip('\r\n'))
                        else:
                            print '%s %s %s' % (str(data[index][0]).rstrip('\r\n'),
                                                str(data[index][1]).rstrip('\r\n'),
                                                str(data[index][2]).rstrip('\r\n'))

            elif directive == 'metadata load police/people/sdryxx -conf mapping.conf ':
                print 'metadata load police/people/sdryxx -conf mapping.conf '
            else:
                print 'invalid command, please check and retry'


    def __login__(self):
        print "input 'login' command to login and go on."
        directive = raw_input('HCOS>')  # get the directive from user
        if directive == 'login':
            userName = raw_input('please input user name:')
            passWord = raw_input('please input password:')
            if CheckUserPassword.check('users.xml', userName, passWord):
                self.isLogIn = True
                print 'login successfully'
            else:
                self.isLogIn = False
                print 'login failed, please check your input and try again!'


if __name__ == '__main__':
    shell = Shell()
    shell.execute()

