# AStar is an artificial intelligence algorithm used to find the shortest
# possible distance from start to ends state

# It could be applied to character path-finding, puzzle solving, etc. ...

# How It Works:

# There are start and goal states. The start state is where yhe program
# begins.

# The goal state is where the program ends.

# It is not always possible to get to the goal state.

# There needs to be a way to measure progress toward our goal.

# There must also be a way to Generate Children or all possible paths to
# a goal.

# Steps towards the Goal

# Step1: Generate a list of all possible next steps towards the goal
# from the current position.

# Step2: Store Children or Paths in a PriorityQueue based on distance to
# goal, closest first.

# Step3: Select closest child and Repeat until the goal is reached or
# there are no more Children.

# !usr/bin/env python

from Queue import PriorityQueue


# everything flows from the State. State is the parent with attributes to
# inherit.

# Attributes value: string, parent: string, start: string, goal: string.
# Value is what the form the object takes at each point from start to goal.

class State(object):
    # State constructor
    def __init__(self, value, parent, start=0, goal=0):
        # default children list, not defined
        self.children = []
        self.parent = parent
        # value of the object at each point in the precess
        self.value = value
        # default distance attribute, not defined
        self.dist = 0
        # if the parent exists
        if parent:
            # take the parents' path as the class path
            self.path = parent.path[:]
            # add parents value to the class value
            self.path.append(value)
            # parents' start becomes class start
            self.start = parent.start
            # parents goal becomes class goal
            self.goal = parent.goal
        # if parent doesn't exist
        else:
            # start a path that is a list of objects, starting with our
            # current value.
            self.path = [value]
            # store the start state.
            self.start = start
            # store the goal state
            self.goal = goal

    # empty function not defined in base class
    def GetDist(self):
        pass

    # empty function not defined in base class
    def CreateChildren(self):
        pass


class State_String(State):
    def __init__(self, value, parent, start=0, goal=0):

        super(State_String, self).__init__(value, parent, start, goal)
        # Override GetDist()
        self.dist = self.GetDist()

    # Define GetDist()
    def GetDist(self):
        # if the parent value ids the same as the goal or
        # if we have reached the goal
        if self.value == self.goal:
            return 0
        # default value of what you are trying to measure set to
        # distance 0
        dist = 0
        # count the position along the length from 1 to x
        for i in range(len(self.goal)):
            letter = self.goal[i]
            # give the absolute value of the i (the goal position
            # of the letters) - the index position (which is the
            # current value position of the letters) 0 to x
            dist += abs(i - self.value.index(letter))
        # return what you are trying to measure
        return dist

    def CreateChildren(self):
        if not self.children:
            # count the position along the length from 1 to x
            for i in range(len(self.goal) - 1):
                # Store value in val
                val = self.value
                # create new value by switching letters at position
                # 1 and 2 for every pair of letters
                val = val[:i] + val[i + 1] + val[i] + val[i + 2:]
                # store instance of State_String in child and pass
                # in val
                child = State_String(val, self)
                # add the new child to the children list
                self.children.append(child)


class AStar_Solver:
    def __init__(self, start, goal):
        # stores the final solution for getting from the start state
        # to the goal state and the exact sequence that it takes to
        # get there
        self.path = []
        # keeps track of all children visited and ensures that we
        # don't visit any children twice
        self.visitedQueue = []
        self.priorityQueue = PriorityQueue()
        # store start state
        self.start = start
        # store goal state
        self.goal = goal

    def Solve(self):
        # the start state has no parent because it is the original so
        # we have to input more specific variables ( current value :
        # self.start, parent : 0, start state : self.start, goal state :
        # self.goal)
        startState = State_String(self.start, 0, self.start, self.goal)
        count = 0
        # priorityQueue organizes
        self.priorityQueue.put((0, count, startState))
        # while the path is empty and the queue has size
        while (not self.path and self.priorityQueue.qsize()):
            # store the next start state of the priorityQueue in
            # closestChild
            closestChild = self.priorityQueue.get()[2]
            # create the child for that state
            closestChild.CreateChildren()
            # add the child to the visited queue
            self.visitedQueue.append(closestChild.value)
            # iterate through the children
            for child in closestChild.children:
                # if the child is not in the visited queue
                if child.value not in self.visitedQueue:
                    # add 1 to the count
                    count += 1
                    # the child distance is zero and therefore does
                    # not exist
                    if not child.dist:
                        # we have found the solution
                        # set the self.path to the child.path
                        self.path = child.path
                        # when the path is set we break out of the if
                        # statement, which sends us back to the while
                        # loop. When the path is set in the while loop
                        # we break out of that loop
                        break
                    self.priorityQueue.put((child.dist, count, child))
        # if we loop through all the children without a match
        if not self.path:
            # print this output error message
            print "Goal of  " + self.goal + " is not possible!"
        return self.path


##============================================
# MAIN

# are we in the main file
if __name__ == '__main__':
    # create a start variable
    start1 = "cdabfe"
    # create a goal variable
    goal1 = "abcdef"
    print "Starting ...."
    # initialize an instance of solver
    a = AStar_Solver(start1, goal1)
    # run the solve function
    a.Solve()
    # output the results
    for i in xrange(len(a.path)):
        print "%d) " % i + a.path[i]
