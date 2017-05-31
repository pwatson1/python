# what are nesting functions? Functions that are
# declared within other Functions
'''
def outside():
    def printHam():
        print "ham"
    return printHam

myFunc = outside()
myFunc()
'''

'''
# why nest a function within a function?
def outside():
    # this acts like a class for the subfunctions
    # you can think of each function as an object

    # x is created in local space for the outside()
    # function. After it executes the printHam() function
    # it no longer exists.
    x = 5
    def printHam():
        print x
    return printHam

myFunc = outside()
myFunc()

# reasons for using nested functions
# less code than classes

# do not have to know what function you are calling just
# add () like myFunc

# can use if, Else, Elif to CHOOSE which function is returned
'''

'''
# passing x through the outside() function works the same as
# the global
def outside(x = 5):
    def printHam():
        print x
    return printHam

# you can also override the passed in variable as well
myFunc = outside(7)
myFunc()
'''

'''
# passing a function into another function
# a decorator for oldFunc
def addOne(myFunc):
    def addOneInside():
        return myFunc() +1
    return addOneInside

def oldFunc():
    return 3

newFunc = addOne(oldFunc)
print oldFunc(), newFunc()
'''

'''
# we can have the results of the old function be replaced
# by the results of the new function whenever we call oldFunc
def addOne(myFunc):
    def addOneInside():
        return myFunc() +1
    return addOneInside

def oldFunc():
    return 3

oldFunc = addOne(oldFunc)
print oldFunc()
'''


def addOne(myFunc):
    # by adding *arhs and **kwargs you can handle most
    # functions passed in
    def addOneInside(*args, **kwargs):
        return myFunc(*args, **kwargs) +1
    return addOneInside

# by using the @addOne declaration we no longer need
# the oldFunc = addOne(oldFunc) line from below and the
# decorator still works.
@addOne
def oldFunc(x=3):
    return x

# values can always be overridden at output
print oldFunc(654)
