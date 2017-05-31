# Exception handling trys to prevent code from breaking
# It has two parts the 'try' and the 'except'
# 'try' TO Execute the code below
# 'except' catches all errors or can catch specific errors
Ex. broken code
x = 5 + "ball"

# Ecxeption handler
try:
    x = 5 + "ball"
except:
    print "darn it!"

# Handler 2
try:
    x = 5 + "ball"
except:
    pass


# the raise key word is used to force a specific error
# to be occur
#      error class | specific error
raise TypeError("hahahahaha")
# when you raise an error it returns an actual error message

# Finally is the last actions to be performed sfter try and
# but before any real errors are returned
try:
    x = 5 + "ball"
except ZeroDivisionError:
    print "will not see this"
finally:
    print "the final word"
