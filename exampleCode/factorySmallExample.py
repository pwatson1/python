# Why use a factory?
# 1 - It allows programs to determine which functions to create
# 2 - It removes duplication of code within multiple classes
# 3 - It can provide functions access to information the classes
# don't have

# in this example we start by using type classing to create
# the classes

BaseClass = type("BaseClass", (object,), {})
C1 = type("C1", (BaseClass,), {"x":1})
C2 = type("C2", (BaseClass,), {"x":30})

# We define a method for the BaseClass
def MyFactory(myBool):
# shortcut conditional
    return C1() if myBool else C2()

    m = MyFactory(True)
    v = MyFactory(False)

    print m.x
    print v.x
