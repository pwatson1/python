# type class creation is an alternate way of creating classes
'''
class MyClass(object):
    def __init__(self):
        self.x = 5

# 1 - a type class consists of three parts the Name, a tuple, and
# an argument in the for of variables or functions
# 2 - The tuple value needs to be followed by a comma inside the parenthesis
# so that python can recognise it as a tuple
TypeClass = type("TypeClass", (object,), {"x":5})
# 3 - create an instance of a regular class
m = MyClass()
# 4 - create an instance of a type class
t = TypeClass


print m.x
print t.x
'''
def printHam(self):
    print "ham"


TypeClass = type("TypeClass", (object,), {"x":5, "printHam": printHam})


t = TypeClass()
# printHam is a bound method and must be called t.printHam()
t.printHam()
# x is an unbound method and can be output with print
print t.x

# This allows for the creation of classes on the fly with less
# lines of code
