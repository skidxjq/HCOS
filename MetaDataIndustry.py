import xml.dom.minidom


def getAllMetadataIndustryType(configFilePath):
    domTree = xml.dom.minidom.parse(configFilePath)

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