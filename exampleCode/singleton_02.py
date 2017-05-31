# A singleton is a design pattern that you use when you only want
# one of something. Ex. one sun, one earth, and you want all
# changes in value in your program should impact the singleton.
# This singleton is considered more efficient and uses decorators

# 1 - creating a decorator
def singleton(myClass):
    # 2 - creating a dictionary that binds all of classes to instances
    # of the classes in memory
    # 3 - check to see if instances has been set
    # 7 - every instance in the future will point to the exact same one
    instances = {}

    def getInstance(*args, **kwargs):
        # 4 - if there is no class already created for the instance
        if myClass not in instances:
            # 5 - create a pairing between the instance and the class
            instances [myClass] = myClass(*args, **kwargs)
        # 6 - return the ordered pairing
        return instances [myClass]
    return getInstance

    # 8 - this is the class that is declared to be passed into singleton()
    @singleton
    class TestClass(object):
        pass

    x = TestClass()
