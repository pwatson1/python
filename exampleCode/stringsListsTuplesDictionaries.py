# Strings are a bunch of characters using quotation marks
# the convention is single quotes foe characters and double
# quotes for full words and sentences

x = "hello"
x

# you can add strings together like integers

y = x + "book"
y

# if you want the words to be spaced, you must include a space

y = x + " book"
y

# You cannot ad a string and a  number together
# but you can use the str prefix to convert a number to
# a strings

z = 10
y = x + str(z)
y

# Special Characters %d for digits, %f for float, limit float
# with a point ex. %.3f,
y = "something %d" %z
y

# use \n for new line, and \t for tab with the print command

x = "ap\n\nple"
x
print x

y = "te\t\tst"
y
print y

# Conditionals using in returns true or false
"an" in "banana"

# Lists using square brackets []
x=[]
x

x = ["ham", 4, 2.2]
x

# List functions
# add values to the end of a list with .append()
x.apend(6)
x

# add to a specific place in the list with .insert()
# arguments are position an then value
x.insert(1, 7.23)
x

# remove an object from a list with .pop()
# argument gives position
x.pop(1)
x

# check for the length of container ... a string or a list
len(x)
# or
len("words")

# List conversion function converts parts of an object into
# a list of items
list("plane")

# will be converted into ['p', 'l', 'a', 'n', 'e']

# you can also apend to an empy list
x = []
x.append("boat")

# You can use the conditional if in with a list. It returns true
# or false

# Tuples are lists that fixed
x = ()
x = ("ham", 4, 5)

# You can't append, insert, pop a tuple

# Dictionaries are a way of binding a key to a value
sam = {}

# add items and assign or reassign value
sam["power"] = "flying"
sam["health"] = 10

# if we call sam the result is {'power':'flying', 'health':10}

# retrieve value
sam[power]

# result 'flying'

# remve items from the dictionary
del sam["power"]
