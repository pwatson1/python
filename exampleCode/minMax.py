# Min Max Algorithm
# Designed for perfect information games like checkers or chess where the
# computer can see everything that is going on. There is no mistery. It may
# not work as well for card games. The win and lose states of the game are
# represented by positive and negative infinity. The algorithm is designed
# to decide what is the best move for each player when it is their turn.

# this program focuses on games that only have two players. Each payer is
# represented by positive and negative 1 where positive 1 is human and
# negative 1 is the computer.

# Checkers
# Create a tree of all possible moves for all players to a certain depth
# Each position or node of the tree holds a Heuristic value - the state
# of the game in a single value

# A winning move is represented by positive infinity
# a losing move is represented by negative infinity

# When the tree is created the algorithm starts at the botom of the tree
# it choses the best decision and eliminates all others at that level

# Stick game
# 1 - Each player takes turns picking up either one or two sticks
# 2 - The goal is to pick up the last sticks
# 3 - If you try to pick up two when only one remains you loose

from sys import maxsize


##============================================
# Tree Builder
class Node(object):
    def __init__(self, i_depth, i_playerNum, i_sticksRemaining, i_value=0):
        self.i_depth = i_depth
        self.i_playerNum = i_playerNum
        self.i_sticksRemaining = i_sticksRemaining
        self.i_value = i_value
        self.children = []
        self.CreateChildren()

    def CreateChildren(self):
        if self.i_depth >= 0:
            for i in range(1, 3):
                v = self.i_sticksRemaining - i
                self.children.append(Node(self.i_depth - 1, - self.i_playerNum, v,
                                          self.RealVal(v)))

    def RealVal(self, value):
        if value == 0:
            return maxsize * self.i_playerNum
        elif value < 0:
            return maxsize * -self.i_playerNum
        return 0


##============================================
# Algorithm
def minMax(node, i_depth, i_playerNum):
    if i_depth == 0 or abs(node.i_value) == maxsize:
        return node.i_value

    i_bestValue = maxsize * -i_playerNum

    for i in range(len(node.children)):
        child = node.children[i]
        i_val = minMax(child, i_depth - 1, -i_playerNum)
        if abs(maxsize * i_playerNum - i_val) < abs(maxsize * i_playerNum
                                                            - i_bestValue):
            i_bestValue = i_val

    return i_bestValue


##============================================
# Implementation
def WinCheck(i_sticks, i_playerNum):
    if i_sticks <= 0:
        print "*" * 30
        if i_playerNum > 0:
            if i_sticks == 0:
                print "\tYou Win!!!"
            else:
                print "\tTOO MANY! You lose..."
        else:
            if i_sticks == 0:
                print "\tComp Wins! Better luck next time."
            else:
                print "\tComp Error!"
        print "*" * 30
        return 0
    return 1


if __name__ == '__main__':
    i_stickTotal = 11
    i_depth = 4
    i_curPlayer = 1
    print """ INSTRUCTIONS: Be the player to pick up the last stick.
    \t\t\tYou can only pick up one (1) or two (2)
    \t\t\tsticks at a time."""

    while i_stickTotal > 0:
        print "\n%d sticks remain. How many would you like to pick up?" % i_stickTotal
        i_choice = input("\n1 or 2: ")
        i_stickTotal -= int(float(i_choice))
        if WinCheck(i_stickTotal, i_curPlayer):
            i_curPlayer *= -1
            node = Node(i_depth, i_curPlayer, i_stickTotal)
            bestChoice = -100
            i_bestValue = -i_curPlayer * maxsize
            for i in range(len(node.children)):
                n_child = node.children[i]
                i_val = minMax(n_child, i_depth, -i_curPlayer)
                if abs(i_curPlayer * maxsize - i_val) <= abs(i_curPlayer * maxsize - i_bestValue):
                    i_bestValue = i_val
                    bestChoice = i
            bestChoice += 1
            print "Comp chooses: " + str(bestChoice) + "\tBased on value: " + str(i_bestValue)
            i_stickTotal -= bestChoice
            WinCheck(i_stickTotal, i_curPlayer)
            i_curPlayer *= -1
