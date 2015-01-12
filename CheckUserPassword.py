import xml.dom.minidom
import FileUtil


def check(configFilePath, userName, password):
    if not FileUtil.isFileValid(configFilePath, '.xml'):
        print 'user config file path is not valid, please check.'
        return

    domTree = xml.dom.minidom.parse(configFilePath)
    collection = domTree.documentElement
    users = collection.getElementsByTagName("user")

    for user in users:
        userNameGot = user.getElementsByTagName('userName')[0].childNodes[0].data
        passwordGot = user.getElementsByTagName('passWord')[0].childNodes[0].data
        if userName == userNameGot and str(password) == passwordGot:
            return True
    return False


if __name__ == '__main__':
    print check('users.xml', 'bob', 123)