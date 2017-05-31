# Override replaces variables in the
# base class with an inherited variable
# have the same name and be spelled
# the exact same way.



class BaseClass(object):
    def __init__(self):
        # Default variable from parent
        # having a default variable insures the program doesn't
        # crash
        self.x = 10


class InClass(BaseClass):
    def __init__(self):
        super(InClass, self).__init__()
        # Overriding variable from child class
        # the child class has the option of overriding or not
        self.x = 20


i = InClass()
print i.x
# a way that you can figure out what classes inherit
# from the base class 
print BaseClass.__subclasses__()
