# Functions are a way of combining a collection of actions
# into a single process for reuse
def doesNothing():
    pass

    doesNothing()

def makeOne():
    return 1

x = makeOne()
print x


# Arguments are a way to INPUT or pass in data to  a
# function
# There are two types of arguments "regular args" and
# "keyword args"
# Regular arguments can be anything: class instances,
# numbers, strings, variables, lists, dictionaries, etc...
# Keyword arguments are key:value pairs identified by
# the keyword or character folloewed by an equal sign
# and an assigned value. This becomes the default value
# that may be overriden at a later time
Ex.
def addTen(myInt):
    myInt+=10
    return myInt

# declare a variable to pass into the function
x = 12

# the 'x' below that is being passed into addTen() is only
# a copy of 'x=12' that was declared. This is important
# because 'myInt' is a local variable and local variables
# do not exist outside the scope of the function as opposed
# to global variables
y = addTen(x)

print x,y
