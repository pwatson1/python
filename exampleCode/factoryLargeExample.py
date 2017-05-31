# Why use a factory?
# 1 - It allows programs to determine which functions to create
# 2 - It removes duplication of code within multiple classes
# 3 - It can provide functions access to information the classes
# don't have

# in this example we start by using type classing to create
# the classes

BaseClass = type("BaseClass", (object,), {})

@classmethod
def Check1(self, myStr):
    return myStr == "ham"

@classmethod
def Check2(self, myStr):
    return myStr == "sandwich"

C1 = type("C1", (BaseClass,), {"x":1, "Check":Check1})
C2 = type("C2", (BaseClass,), {"x":30, "Check":Check2})

# We define a method for the BaseClass
def MyFactory(myStr):
# for each cls in the subclasses of BaseClass
    for cls in BaseClass.__subclasses__():
# if you call the function Check() and pass in the myStr
# argument. If it is True,other wise if the string is a valid
# value for myStr ...
        if cls.Check(myStr):
# create an instance of that class and return it
            return cls()


    m = MyFactory(True)
    v = MyFactory(False)

    print m.x
    print v.x
