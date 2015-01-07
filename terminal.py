# This is the Command Line Interface(CLI) of the project.
import CheckUserPassword
import MetaDataIndustry


class Shell(object):
    # todo make it False
    isLogIn = True

    def __init__(self):
        pass

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
                print 'metadata get police'
            elif directive == 'metadata get police/people':
                print 'metadata get police/people'
            elif directive == 'metadata get police/people/sdryxx':
                print 'metadata get police/people/sdryxx'
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
