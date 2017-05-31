# Functions take in arguments. We use *args to take
# an unlimited number of regular arguments when you
# don't know how many to take. It also prevents the
# peogram from crashing

'''
def Func(*args):
    for arg in args:
        print arg

Func(1, 2, 3, 54, "ham")
'''

'''
def Func(*args):
    for arg in args:
        print arg

l = [1, 2, 3, 54, "ham"]
# when you call the variable, pyuthon prints the list
Func(l)
'''

'''
def Func(*args):
    for arg in args:
        print arg

l = [1, 2, 3, 54, "ham"]
# when you place a * in front of the variable, python
# prints the individual items
Func(*l)
'''

'''
The x=234 and y=9 are kwargs

def Func(x=234, y=9):
    print x,y

Func()
# this works because kwargs provid default values
'''

'''
def Func(x=234, y=9):
    print x,y

# the kwargs can be overridden in the function call
Func(x=456, y=3)
'''

'''
def Func(**kwargs):
    # because python interprets the kwargs like a dictionary
    # we call it as if it were a dictionary
    for item in kwargs.items():
        print item

# the answer prints out both the key and the value
Func(x=456, y=3)
'''


def Func(*args, **kwargs):
    for arg in args:
        print arg

    for item in kwargs.items():
        print item

# the args and kwargs must be passed into the function
# and the function call in the same order
Func(1, 2, 3, 54, "ham", x=456, y=3)
