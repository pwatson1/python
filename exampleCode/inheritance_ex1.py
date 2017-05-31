# Object oriented programing based around classes and
# instances of those classes (aka Objects)

# How do classes interact and Directly effect one another?
# Inheritence - when one class gains all the attributes of
# another class

# BaseClass is the parent class
# Must use object so the child class can refer to its attributes
class BaseClass(object):
    # passing in self makes BaseClass the owner of the function
    def printHam(self):
        print 'Ham'


# passing in BaseClass makes InheritingClass the child class
# of BaseClass and allows InheritingClass to inherit  BaseClasses
# attributes
class InheritingClass(BaseClass):
    pass


# creating an instance of InheritingClass
# InheritingClass has all the attributes of BaseClass
x = InheritingClass()
# so even though it doesn't have a printHam function you can
# still call the function
x.printHam()
