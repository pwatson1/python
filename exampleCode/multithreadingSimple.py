# Multithreading

# Multithreading is running multiple tasks in parallel to each other on
# the same cpu

# Where to use multithreading?

# 1 - On tasks that run pretty much independent of each other
# 2 - Ex. physics/collision calculations on one thread and graphics
# calculations on another thread.
# 3 - All threads should communicate back with the main thread.

# What to avoid

# Avoid having a thread change or delete another thread is using

# How to use it

# There are two modules "thread" and "threading"
# thread is the older module but is considered outdated
# threading is considered better and has more features

import random
import threading


def Splitter(words):
    mylist = words.split()
    newList = []
    while mylist:
        newList.append(mylist.pop(random.randrange(0, len(mylist))))
        print ''.join(newList)


if __name__ == '__main__':
    sentence = 'I am a handsome beast. words'
    numOfThreads = 5
    threadList = []

    print "Starting...\n"
    for i in range(numOfThreads):
        t = threading.Thread(target=Splitter, args=(sentence,))
        t.start()
        threadList.append(t)

    print "\nThreadCount: " + str(threading.activeCount())
    print "Exiting...\n"
