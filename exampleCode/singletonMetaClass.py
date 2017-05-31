# Chapter 17
class Singleton(type):
# _instance is just a container name for the dictionary
# but it makes it easier to foloow what's happening
    _instances = {}
# this function uses cls instead of self . Unlike self which refers
# to the parent class, cls refers to any class
    def __call__(cls, *args, **kwargs):
# this says. "if the class does not exist...
        if cls not in cls._instances:
# use the parent singleton class to make it
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
# create an instance with a value of 5
            cls.x = 5
# Output that instance
        return cls._instances[cls]


class MyClass(object):
# when this class is defined, we want python to search for a
# __metaclass__ definition which prevents other classes from
# inheriting its attributes. Therefore there can only be one of
# this class which satisfies the singleton definition.

# when the class is created it will be created based on the
# singleton method 
    __metaclass__ = Singleton

# By creating m and v instances we can test to see if they are
# actually the same block of memory
m = MyClass()
v = MyClass()
print m.x
m.x = 9
print v.x
