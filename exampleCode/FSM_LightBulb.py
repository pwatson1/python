from random import randint
from time import clock

##============================================
# STATE
# Create a State base class
State = type("State", (object,), {})


# first state for the light
class LightOn(State):
    def Execute(self):
        print "Light is ON"


# second state for the light
class LightOff(State):
    def Execute(self):
        print "Light if OFF"


##============================================
# TRANSITION
class Transition(object):
    def __init__(self, toState):
        self.toState = toState

    def Execute(self):
        print "Transitioning ....."


##============================================
# FSM: Default variables
class SimpleFSM(object):
    def __init__(self, char):
        self.char = char
        self.states = {}
        self.transitions = {}
        self.curState = None
        self.trans = None

    def SetState(self, stateName):
        # pairs the current state with the passed in state and adds
        # it to the states dictionary
        self.curState = self.states[stateName]

    def Transition(self, transName):
        # pairs the transition with the passed in transName and adds
        # it to the states dictionary
        self.trans = self.transitions[transName]

    def Execute(self):
        if (self.trans):
            self.trans.Execute()
            self.SetState(self.trans.toState)
            self.trans = None
        self.curState.Execute()


##============================================
# Character Class
class Char(object):
    def __init__(self):
        # FSM contained in character class
        self.FSM = SimpleFSM(self)
        self.LightOn = True


##============================================
if __name__ == "__main__":
    light = Char()

    light.FSM.states["On"] = LightOn()
    light.FSM.states["Off"] = LightOff()
    # Transition passes string into light.FSN.states, the container
    # for the new instance
    light.FSM.transitions["toOn"] = Transition("On")
    light.FSM.transitions["toOff"] = Transition("Off")

    light.FSM.SetState("On")

    for i in xrange(20):
        startTime = clock()
        timeInterval = 1
        while startTime + timeInterval > clock():
            pass
        if randint(0, 2):
            if light.LightOn:
                print "Transitioning"
                light.FSM.transitions["toOff"]
                light.FSM.SetState("Off")
                light.LightOn = False
            else:
                light.FSM.transitions["toOn"]
                print "Transitioning"
                light.FSM.SetState("On")
                light.LightOn = True
        light.FSM.Execute()

##============================================
