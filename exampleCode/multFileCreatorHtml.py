import time as t
from os import path


def createFile(dest):
    '''

    The script creates a text file at the passed in location ,
    names file based on date
    '''

    date = t.localtime(t.time())

    words = '\nWriting code that creates files' * 30

    # FileName = Month_Day_Year

    name = '%d_%d_%d.html' % (date[1], date[2], (date[0] % 100))

    # if not (path.isfile(dest + name)):
    for i in range(5):
        f = open(dest + str(i) + '_' + name, 'w')
        f.write(words)
        f.close()


if __name__ == '__main__':
    destination = 'E:\\python projects\\python_work\\letsLearn\\'
    createFile(destination)
    print 'Writing code that creates files'
    raw_input('done!!!')
