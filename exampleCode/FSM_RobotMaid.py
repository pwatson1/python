from random import randint
from time import clock


##===================================
# TRANSITION
class Transition(object):
    def __init__(self, toState):
        self.toState = toState

    def Execute(self):
        print "Transitioning ....."


##==================================
# STATE
class State(object):
    def __init__(self, FSM):
        self.FSM = FSM
        self.timer = 0
        self.startTime = 0

    # Enter is only called when there is a transition happening
    def Enter(self):
        self.timer = randint(0, 5)
        self.startTime = int(clock())

        def Execute(self):
            pass

        # Exit is only called when there is a transition happening
        def Exit(self):
            pass


# in the constructor of CleanDishes I call the constructor of the
# base State class. "super("CleanDishes", self).__init__(FSM). I pass
# in FSM so we can make adjustments and grab data from it.
class CleanDishes(State):
    def __init__(self, FSM):
        super(CleanDishes, self).__init__(FSM)

    def Enter(self):
        print "Preparing to clean dishes"
        # initiate the Enter function from the inherited State which
        # will create a simple timer as in the parent
        super(CleanDishes, self).Enter()

    def Execute(self):
        print "Cleaning dishes"
        if (self.startTime + self.timer <= clock()):
            if not (randint(1, 3) % 2):
                # self.FSM triggers the Finite State Machine to do something
                self.FSM.ToTransition("toVacuum ")
            else:
                # self.FSM triggers the Finite State Machine to do something
                self.FSM.ToTransition("toSleep")

    def Exit(self):
        print "Finished cleaning dishes"


# in the constructor of CleanDishes I call the constructor of the
# base State class. "super("Vacuum", self).__init__(FSM). I pass
# in FSM so we can make adjustments and grab data from it.
class Vacuum(State):
    def __init__(self, FSM):
        super(Vacuum, self).__init__(FSM)

    def Enter(self):
        print "Preparing to vacuum"
        # initiate the Enter function from the inherited State which
        # will create a simple timer as in the parent
        super(Vacuum, self).Enter()

    def Execute(self):
        print "Vacuuming the floor"
        if (self.startTime + self.timer <= clock()):
            if not (randint(1, 3) % 2):
                # self.FSM triggers the Finite State Machine to do something
                self.FSM.ToTransition("toSleep ")
            else:
                # self.FSM triggers the Finite State Machine to do something
                self.FSM.ToTransition("toCleanDishes")

    def Exit(self):
        print "Finished vacuuming"


# in the constructor of CleanDishes I call the constructor of the
# base State class. "super("Sleep", self).__init__(FSM). I pass
# in FSM so we can make adjustments and grab data from it.
class Sleep(State):
    def __init__(self, FSM):
        super(Sleep, self).__init__(FSM)

    def Enter(self):
        print "Starting to sleep"
        # initiate the Enter function from the inherited State which
        # will create a simple timer as in the parent
        super(Sleep, self).Enter()

    def Execute(self):
        print "Sleeping"
        if (self.startTime + self.timer <= clock()):
            if not (randint(1, 3) % 2):
                # self.FSM triggers the Finite State Machine to do something
                self.FSM.ToTransition("toVacuum ")
            else:
                # self.FSM triggers the Finite State Machine to do something
                self.FSM.ToTransition("toCleanDishes")

    def Exit(self):
        print "Waking up from sleep"


##============================================
# Finite State Machine
class FSM(object):
    def __init__(self, character):
        self.char = character
        self.states = {}
        self.transitions = {}
        self.curState = None
        self.prevState = None  # prevents code from looping on itself
        self.trans = None

    def AddTransition(self, transName, transition):
        self.transitions[transName] = transition

    def AddState(self, stateName, state):
        self.prevState = self.curState

    def SetState(self, stateName):
        self.prevState = self.curState
        self.curState = self.states[stateName]

    def ToTransition(self, toTrans):
        self.trans = self.transitions[toTrans]

    def Execute(self):
        if (self.trans):
            self.curState.Exit()
            self.trans.Execute()
            self.SetState(self.trans.toState)
            self.curState.Enter()
            self.trans = None
        self.curState.Execute()


##============================================
# Implementation
Char = type("Char", (object,), {"day": 0})


class RobotMaid(Char):
    def __init__(self):
        super(RobotMaid, self).__init__()
        self.FSM = FSM(self)

        # STATE
        self.FSM.AddState("Sleep", Sleep(self.FSM))
        self.FSM.AddState("CleanDishes", CleanDishes(self.FSM))
        self.FSM.AddState("Vacuum", Vacuum(self.FSM))

        # TRANSITION
        self.FSM.AddTransition("toSleep", Transition("Sleep"))
        self.FSM.AddTransition("toVacuum", Transition("Vacuum"))
        self.FSM.AddTransition("toCleanDishes", Transition("CleanDishes"))

        self.FMS.SetState("Sleep")

    def Execute(self):
        self.FSM.Execute()


if __name__ == "__main__":
    r = RobotMaid()
    for i in xrange(10):
        startTime = clock()
        timeInterval = 1
        while startTime + timeInterval > clock():
            pass
        r.Execute()
