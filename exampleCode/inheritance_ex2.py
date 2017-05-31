# Object oriented programing based around classes and
# instances of those classes (aka Objects)

# How do classes interact and Directly effect one another?
# Inheritence - when one class gains all the attributes of
# another class
class Character(object):
    # the init function runs when the Character class is called
    def __init__(self):
        self.health = 100


# passing in Character makes Blacksmith the child class
# of Character and allows Blacksmith to inherit  Character
# attributes
class Blacksmith(Character):
    # the init function runs when the Blacksmith class is called
    def __init__(self):
        # the super function refers back to the parent Character and
        # calls the parent's, Character's init function
        super(Blacksmith, self).__init__()


# create an instance of Blacksmith
bs = Blacksmith()
print bs.health
