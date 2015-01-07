import xml.dom.minidom
import FileUtil


def getAllMetadataIndustryType(configFilePath):
    domTree = xml.dom.minidom.parse(configFilePath)
    if not FileUtil.isFileValid(configFilePath, '.xml'):
        print 'metadata industry config file path is not valid, please check.'
        return
    collection = domTree.documentElement
    types = collection.getElementsByTagName('industryType')
    typesArray = []

    for dataType in types:
        typeName = dataType.childNodes[0].data
        typesArray.append(typeName)
    return typesArray


if __name__ == '__main__':
    types = getAllMetadataIndustryType('metadataIndustry.xml')
    for type in types:
        print type