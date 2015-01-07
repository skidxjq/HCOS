import os


class JavaDirective(object):
    is_created_successfully = False

    def __init__(self, file_path):
        self.filePath = file_path
        self.__check_file_path()

    def __check_file_path(self):
        self.is_created_successfully = os.path.isfile(self.filePath) and self.filePath.endswith('.java')
        if not self.is_created_successfully:
            print 'invalid file path, please input again'

    def javac(self):
        if self.is_created_successfully:
            result_int = os.system('javac ' + self.filePath)
            if result_int == 0:
                print 'java file compiled successfully'
            else:
                print 'java file compiled failed'

    def java(self):
        if self.is_created_successfully:
            result_int = os.system('java ' + self.filePath[:-len('.java')])
            if result_int == 0:
                print 'java file executed successfully'
            else:
                print 'java file executed failed'


if __name__ == '__main__':
    a = JavaDirective('b.java')
    print a.is_created_successfully
    a.javac()
    a.java()