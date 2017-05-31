# Object oriented programing based around classes and
# instances of those classes (aka Objects)

# How do classes interact and Directly effect one another?
# Inheritence - when one class gains all the attributes of
# another class
# class inherits from object
class Character(object):
    # the init function runs when the Character class is called
    # by passing in the name parameter
    def __init__(self, name):
        # self.health is an optional attribute of the class
        self.health = 100
        # self.name is required because we passed in name
        # self.name is the container. There is no requirement that we
        # call this self.name we can call it self,applesauce if we like
        self.name = name

    # another function but not initialized at call
    def print_name(self):
        print self.name


# passing in Character makes Blacksmith the child class
# of Character and allows Blacksmith to inherit  Character
# attributes
class Blacksmith(Character):
    # the init function of the child class should at least have the
    # parameters of the parent classes init function
    def __init__(self, name, forgeName):
        # the super function refers back to the parent Character and
        # calls the parent's, Character's init function and we want to
        # pass in the parameters that are associated with it
        super(Blacksmith, self).__init__(name)
        # self.forge is required because we passed in forgeName
        # self.forge is the container. There is no requirement that we
        # call this self.forge we can call it self,applesauce if we like
        # an example of taking ownership of an attribute that is part of
        # a class you don't inherit from
        self.forge = Forge(forgeName)


class Forge:
    def __init__(self, forgeName):
        self.name = forgeName


bs = Blacksmith("Paul", "Old Smokey")
bs.print_name()
print bs.health
print bs.forge.name
