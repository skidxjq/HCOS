import xml.dom.minidom
import FileUtil


def __getConfRoot(configFilePath, nodeName):
    if not FileUtil.isFileValid(configFilePath, '.xml'):
        print 'user config file path is not valid, please check.'
        return

    domTree = xml.dom.minidom.parse(configFilePath)
    collection = domTree.documentElement
    root = collection.getElementsByTagName(nodeName)
    # node = mappingNode.getElementsByTagName(attributeName)[0].childNodes[0].nodeValue
    return root[0]


def getElement(configFilePath, rootNode, nodeName):
    return __getConfRoot(configFilePath, rootNode).getElementsByTagName(nodeName)[0].childNodes[0].data


print getElement('./config/config.xml', 'DatabaseConfig', 'host')