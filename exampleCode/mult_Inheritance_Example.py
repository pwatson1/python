# inheritence from multiple base classes
from abc import ABCMeta, abstractmethod


# abstract classes prevents the base class from
# being instantiated. Abstract classes can be used
# to create multiple inheritance

# It forces functions with EXACT names
# to be defined and named in a way that
# will allow for override

class Enemy(object):
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
    def attackPlayer(self, player):
        pass


class EnvironmentAsset(object):
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
    def __init__(self):
        self.mobile = false


# this class inherits from the two abstract classes
class Trap(Enemy, EnvironmentAsset):
    def __init__(self):
        # super references the parent and  calls the parents init
        # function
        supper(Trap, self).__init__()

    # this method overrides attackPlayer from the parent
    def attackPlayer(self, player):
        return player.health - 10

        x = Trap()
