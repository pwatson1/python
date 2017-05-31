class Test:
	pass
x = Test()

class PH:
	def __init__(self):
		self.y = 5     # global var
		z = 5          # local var
	def printHam(self):
		print 'Ham'
	
x = PH()
x.printHam()     # called externally at runtime

============================================================================

class PH:
	def __init__(self):
		self.y = 5     global var
		z = 5          local var
		self.printHam()  # created internally at initialization 
		
	def printHam(self):
		print 'Ham'

		
=============================================================================

class Hero:
	def __init__(self, name):
		self.name = name
		self.health = 100
		
	def eat(self, food):
		if food == 'apple':
			self.health -= 100
		elif food == 'ham':
			self.health += 20
	
Bob = Hero('Bob')

print Bob.name
print Bob.health

Bob.eat('apple')
print Bob.health