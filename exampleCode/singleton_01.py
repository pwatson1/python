# A singleton is a design pattern that you use when you only want
# one of something. Ex. one sun, one earth, and you want all
# changes in value in your program should impact the singleton
# this singleton uses the .__new__() function and avoids the
# __init__() function

# 1 - create a class called MySingleton and save it in memory
class MySingleton(object):
    # 3 - check to see if instance has been set
    # 7 - every instance in the future will point to the exact same one
    _instance = None
    # 2 - call the constructor
    def  __new__(self):
        # 4 - if there is no value in _instance
        if not self._instance:
            # 5 - create an _instance
            # 8 - don't use __init__ because it duplicates the creation of
            # the instance created by the __new__
            self._instance = super(MySingleton, self).__new__(self)
            # 9 - an init function would call the variable every time an instance
            # is created and there would be no conditional
            self.y = 10
        # 6 - return the _instance
        return self._instance

x = MySingleton()
print x.y
x.y=20
z = MySingleton()
print z.y
