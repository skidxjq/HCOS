# This is the Command Line Interface(CLI) of the project.
import CheckUserPassword


class Shell(object):
    isLogIn = False

    def __init__(self):
        pass

    def execute(self):
        directive = ''
#         print"""----------------------------------------------------------
#     welcome
# ----------------------------------------------------------"""
        while directive != 'quit':
            directive = raw_input('HCOS>')  # get the directive from user
            if directive == 'login':
                userName = raw_input('please input user name:')
                passWord = raw_input('please input password:')
                if CheckUserPassword.check(userName, passWord):
                    print 'login successfully'
                else:
                    print 'login failed, please check your input and try again!'


if __name__ == '__main__':
    shell = Shell()
    shell.execute()
