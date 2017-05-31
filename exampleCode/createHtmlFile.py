# Creating text files allows you to create other files in python
# or other languages especially if there are lots of files using
# a lot of the same code
# *** Write scripts that write other scripts ***

# this program will create a HTML file that has a date as a name
# and the text file will have 30 blank lines

# access the time module import time as t
import time as t
# access the path function in the os module. It verifies that
# the file is not already created. if the script is called again
# after it is run once we are not overriding the text file that is
# already in existence
from os import path


def createFile(dest):
    '''

    The script creates a text file at the passed in location ,
    names file based on date
    '''

    # importing time allows you to access time fuctions. We start
    # with current time function and then specify local time
    date = t.localtime(t.time())

    words = '\nWriting code that creates files' * 30

    # this code bases the name of the file on the date in the format of
    # FileName = Month_Day_Year. We take t.time() and give it a text
    # format
    name = '%d_%d_%d.html' % (date[1], date[2], (date[0] % 100))

    # if the file doesnot already exist, create it using dest and name
    if not (path.isfile(dest + name)):
        # creates the file in a writable format and place it in f
        f = open(dest + name, 'w')
        f.write(words)
        f.close()


# verifies ther is no other main file
if __name__ == '__main__':
    destination = 'E:\\python projects\\python_work\\letsLearn\\'
    createFile(destination)
    # the print line will show on the HTML page
    print 'Writing code that creates files'
    # the input line will show in terminal
    raw_input('done!!!')
