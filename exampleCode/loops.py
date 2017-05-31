# Loops are a way to repeat a single action over and override
# compared to functions that are a way to repeat a collection
# of actions in a single process

# while loop
x = 0
while(x<10):

# will add by 1 until x is no longer less than 10
    x+=1


# coordinates
x,y = 0,0
while(true):
    x+=1
    y+=2
    if(x+y>10):

# break used to stop a loop
        break


# for loops
x = [1,2,7]

# for every item in the list x, print the item
for i in x:
    print i


# Combining for loops with ranges
# a range creates a sequence of number from zero upto
# but not including the number out in the range
for i in range (30):
# will print all numbers from zero but not the last number 30
    print i

# Create a range with parameters
# arguments are min, max, step size
for i in range (10, 30, 2):
    print i

# skipping past a value and move on to the next increment
for i in range (30):
# if not a multiple of three print in the range
    if not (i%3):
        continue
    print i
