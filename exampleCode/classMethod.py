# this decorator @classmethod allows to call functions
# within classes without having to instantiate them
# Ex. x = MyClass()
class MyClass():
    @classmethod
    def printHam(self):
        print "ham"

MyClass.printHam()
