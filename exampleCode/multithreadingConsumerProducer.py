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

import threading
import time
import random
try:
    import Queue
except:
    import queue as Queue

class Producer:
    def __init__(self):
        self.food = ['ham', 'soup', 'salad']
        self.nextTime = 0

    def run(self):
        global q
        while time.clock() < 10:
            if self.nextTime < time.clock():
                f = self.food[random.randrange(len(self.food))]
                q.put(f)
                print "Adding..." + f
                self.nextTime += random.random()

class Consumer:
    def __init__(self):
        self.nextTime = 0

    def run(self):
        global q
        while time.clock() < 10:
            if self.nextTime < time.clock() and not q.empty():
                f = q.get()
                print "Removing " + f
                self.nextTime += random.random()*2

if __name__ == '__main__':
    q = Queue.Queue(10)

    p = Producer()
    c = Consumer()
    pt = threading.Thread(target=p.run, args=())
    ct = threading.Thread(target=c.run, args=())
    pt.start()
    ct.start()
