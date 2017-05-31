from abc import ABCMeta, abstractmethod

# abstract classes prevents the base class from
# being instantiated

# It forces functions with EXACT names
# to be defined and named in a way that
# will allow for override


class BaseClass(object):
    # setting up the __metaclass__
    # to be a an abstract BaseClass
    # this declares the class as abstract
    __metaclass__ = ABCMeta

    # @abstractmethod is a
    # declaration of the function
    # as abstract
    @abstractmethod
    # decorator. a way to dynamically
    # alter class or functions
    # without having to inherit or
    # subclass
    def printHam(self):
        pass


class InClass(BaseClass):
    def printHam(self):
        print "ham"


# cannot instantiate the base class
# x = BaseClass()

# can instantiate the subclass
x = InClass()
x.printHam()
