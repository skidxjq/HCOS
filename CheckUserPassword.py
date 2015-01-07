import xml.dom.minidom


def check(userName, password):
    domTree = xml.dom.minidom.parse("users.xml")
    collection = domTree.documentElement
    users = collection.getElementsByTagName("user")

    for user in users:
        userNameGot = user.getElementsByTagName('userName')[0].childNodes[0].data
        passwordGot = user.getElementsByTagName('passWord')[0].childNodes[0].data
        if userName == userNameGot and str(password) == passwordGot:
            return True
    return False

if __name__ == '__main__':
    print check('bob',123)