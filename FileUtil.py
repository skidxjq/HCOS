import os


def isFileValid(filePath, endWithString=''):
    if os.path.isfile(filePath) and filePath.endswith(endWithString):
        return True
    else:
        return False