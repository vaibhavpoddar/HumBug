import enum, sys
from pandas import DataFrame, read_csv

GOALS = []

class Edge():
	def __init__(self, edgeType, i, j):
		self.nodes = []
		self.type  = edgeType
		self.i = i
		self.j = j
		if self.type==WALL:
			self.name = "Wall"
		elif self.type==SIMPLE:
			self.name = "Simple"
		else:
			raise Exception("Invalid Edge")

	def __repr__(self):
		if self.type==WALL:
			return "W"
		if self.type==SIMPLE:
			return "."

class Spider():
	def __init__(self, parent, i, j, animalNumber):
		self.parent = parent
		self.name = "Spider"
		self.animalNumber = animalNumber
		self.x = i
		self.y = j
		self.isLive = True
		self.stack = []
		
	def move(self, d, steps, tabs):
		global TABLE
		oldParent = self.parent
		oldParent.isSitting = False
		oldParent.child     = None
		i = oldParent.i
		j = oldParent.j
		if d == MOVE_UP:
			self.parent = TABLE[i-2*steps][j] 
		if d == MOVE_DOWN:
			self.parent = TABLE[i+2*steps][j] 
		if d == MOVE_LEFT:
			self.parent = TABLE[i][j-2*steps] 
		if d == MOVE_RIGHT:
			self.parent = TABLE[i][j+2*steps] 
		
		newparent = self.parent
		newparent.isSitting = True
		newparent.child     = self
		self.x = newparent.i
		self.y = newparent.j
		Goaled = False
		if newparent.isGoal:
			self.isLive = False
			newparent.isGoal = False
			newparent.name = "Plain"
			newparent.isPlain = True
			newparent.isSitting = False
			Goaled = True
		else:
			print(tabs+"Not goaled section")
		self.stack.append((oldParent, newparent, d, Goaled))

		print("{}Spider{} moved \033[0;37;42m{}\033[0m {}".format(tabs,self.animalNumber, direction_dict[d], steps))
		if(Goaled):
			print(tabs+"GOALED!!!!!!!!!!")

	def dismove(self, tabs):
		global TABLE
		(oldParent, newparent, d, Goaled) = self.stack[-1]
		newparent.isSitting = False
		newparent.child = None
		oldParent.isSitting = True
		oldParent.child = self
		self.parent = oldParent
		self.x = oldParent.i
		self.y = oldParent.j
		if Goaled:
			self.isLive = True
			newparent.isGoal = True
			newparent.isPlain = False
			newparent.name = "Goal"
		self.stack.pop()
		print("{}Spider{} UNDO \033[0;37;43m{}\033[0m".format(tabs,self.animalNumber, direction_dict[d]))

	def Contact(self):
		return self.name + "" + str(self.animalNumber)

	def __repr__(self):
		return self.Contact()

class Bug():
	def __init__(self, parent, i, j, animalNumber):
		self.parent = parent
		self.name = "Bug"
		self.animalNumber = animalNumber
		self.x = i
		self.y = j
		self.isLive = True
		self.stack = []
		
	def move(self, d, steps, tabs):
		global TABLE
		oldParent = self.parent
		oldParent.isSitting = False
		oldParent.child     = None
		i = oldParent.i
		j = oldParent.j
		if d == MOVE_UP:
			self.parent = TABLE[i-2*steps][j] 
		if d == MOVE_DOWN:
			self.parent = TABLE[i+2*steps][j] 
		if d == MOVE_LEFT:
			self.parent = TABLE[i][j-2*steps] 
		if d == MOVE_RIGHT:
			self.parent = TABLE[i][j+2*steps] 
		
		newparent = self.parent
		newparent.isSitting = True
		newparent.child     = self
		self.x = newparent.i
		self.y = newparent.j
		Goaled = False
		if newparent.isGoal:
			self.isLive = False
			newparent.isGoal = False
			newparent.name = "Plain"
			newparent.isPlain = True
			newparent.isSitting = False
			Goaled = True
		else:
			print(tabs+"Not goaled section")
		self.stack.append((oldParent, newparent, d, Goaled))

		print("{}Bug{} moved \033[0;37;42m{}\033[0m {}".format(tabs,self.animalNumber, direction_dict[d], steps))
		if(Goaled):
			print(tabs+"GOALED!!!!!!!!!!")

	def dismove(self, tabs):
		global TABLE
		(oldParent, newparent, d, Goaled) = self.stack[-1]
		newparent.isSitting = False
		newparent.child = None
		oldParent.isSitting = True
		oldParent.child = self
		self.parent = oldParent
		self.x = oldParent.i
		self.y = oldParent.j
		if Goaled:
			self.isLive = True
			newparent.isGoal = True
			newparent.isPlain = False
			newparent.name = "Goal"
		self.stack.pop()
		print("{}Bug{} UNDO \033[0;37;43m{}\033[0m".format(tabs,self.animalNumber, direction_dict[d]))

	def Contact(self):
		return self.name + "" + str(self.animalNumber)

	def __repr__(self):
		return self.Contact()

class Grasshopper():
	def __init__(self, parent, i, j, animalNumber):
		self.parent = parent
		self.name = "Grasshopper"
		self.animalNumber = animalNumber
		self.x = i
		self.y = j
		self.isLive = True
		self.stack = []
		
	def move(self, d, steps, tabs):
		global TABLE
		oldParent = self.parent
		oldParent.isSitting = False
		oldParent.child     = None
		i = oldParent.i
		j = oldParent.j
		if d == MOVE_UP:
			self.parent = TABLE[i-2*steps][j] 
		if d == MOVE_DOWN:
			self.parent = TABLE[i+2*steps][j] 
		if d == MOVE_LEFT:
			self.parent = TABLE[i][j-2*steps] 
		if d == MOVE_RIGHT:
			self.parent = TABLE[i][j+2*steps] 
		
		newparent = self.parent
		newparent.isSitting = True
		newparent.child     = self
		self.x = newparent.i
		self.y = newparent.j
		Goaled = False
		if newparent.isGoal:
			self.isLive = False
			newparent.isGoal = False
			newparent.name = "Plain"
			newparent.isPlain = True
			newparent.isSitting = False
			Goaled = True
		else:
			print(tabs+"Not goaled section")
		self.stack.append((oldParent, newparent, d, Goaled))

		print("{}Grasshopper{} moved \033[0;37;42m{}\033[0m {}".format(tabs,self.animalNumber, direction_dict[d], steps))
		if(Goaled):
			print(tabs+"GOALED!!!!!!!!!!")

	def dismove(self, tabs):
		global TABLE
		(oldParent, newparent, d, Goaled) = self.stack[-1]
		newparent.isSitting = False
		newparent.child = None
		oldParent.isSitting = True
		oldParent.child = self
		self.parent = oldParent
		self.x = oldParent.i
		self.y = oldParent.j
		if Goaled:
			self.isLive = True
			newparent.isGoal = True
			newparent.isPlain = False
			newparent.name = "Goal"
		self.stack.pop()
		print("{}Grasshopper{} UNDO \033[0;37;43m{}\033[0m".format(tabs,self.animalNumber, direction_dict[d]))

	def Contact(self):
		return self.name + "" + str(self.animalNumber)

	def __repr__(self):
		return self.Contact()

class Bee():
	def __init__(self, parent, i, j, animalNumber):
		self.parent = parent
		self.name = "Bee"
		self.animalNumber = animalNumber
		self.x = i
		self.y = j
		self.isLive = True
		self.stack = []
		
	def move(self, d, steps, tabs):
		global TABLE
		oldParent = self.parent
		oldParent.isSitting = False
		oldParent.child     = None
		i = oldParent.i
		j = oldParent.j
		if d == MOVE_UP:
			self.parent = TABLE[i-2*steps][j] 
		if d == MOVE_DOWN:
			self.parent = TABLE[i+2*steps][j] 
		if d == MOVE_LEFT:
			self.parent = TABLE[i][j-2*steps] 
		if d == MOVE_RIGHT:
			self.parent = TABLE[i][j+2*steps] 
		
		newparent = self.parent
		newparent.isSitting = True
		newparent.child     = self
		self.x = newparent.i
		self.y = newparent.j
		Goaled = False
		if newparent.isGoal:
			self.isLive = False
			newparent.isGoal = False
			newparent.name = "Plain"
			newparent.isPlain = True
			newparent.isSitting = False
			Goaled = True
		else:
			print(tabs+"Not goaled section")
		self.stack.append((oldParent, newparent, d, Goaled))

		print("{}Bee{} moved \033[0;37;42m{}\033[0m {}".format(tabs,self.animalNumber, direction_dict[d], steps))
		if(Goaled):
			print(tabs+"GOALED!!!!!!!!!!")

	def dismove(self, tabs):
		global TABLE
		(oldParent, newparent, d, Goaled) = self.stack[-1]
		newparent.isSitting = False
		newparent.child = None
		oldParent.isSitting = True
		oldParent.child = self
		self.parent = oldParent
		self.x = oldParent.i
		self.y = oldParent.j
		if Goaled:
			self.isLive = True
			newparent.isGoal = True
			newparent.isPlain = False
			newparent.name = "Goal"
		self.stack.pop()
		print("{}Bee{} UNDO \033[0;37;43m{}\033[0m".format(tabs,self.animalNumber, direction_dict[d]))

	def Contact(self):
		return self.name + "" + str(self.animalNumber)

	def __repr__(self):
		return self.Contact()

class Butterfly():
	def __init__(self, parent, i, j, animalNumber):
		self.parent = parent
		self.name = "Butterfly"
		self.animalNumber = animalNumber
		self.x = i
		self.y = j
		self.isLive = True
		self.stack = []
		
	def move(self, d, steps, tabs):
		global TABLE
		oldParent = self.parent
		oldParent.isSitting = False
		oldParent.child     = None
		i = oldParent.i
		j = oldParent.j
		if d == MOVE_UP:
			self.parent = TABLE[i-2*steps][j] 
		if d == MOVE_DOWN:
			self.parent = TABLE[i+2*steps][j] 
		if d == MOVE_LEFT:
			self.parent = TABLE[i][j-2*steps] 
		if d == MOVE_RIGHT:
			self.parent = TABLE[i][j+2*steps] 
		
		newparent = self.parent
		newparent.isSitting = True
		newparent.child     = self
		self.x = newparent.i
		self.y = newparent.j
		Goaled = False
		if newparent.isGoal:
			self.isLive = False
			newparent.isGoal = False
			newparent.name = "Plain"
			newparent.isPlain = True
			newparent.isSitting = False
			Goaled = True
		else:
			print(tabs+"Not goaled section")
		self.stack.append((oldParent, newparent, d, Goaled))

		print("{}Butterfly{} moved \033[0;37;42m{}\033[0m {}".format(tabs,self.animalNumber, direction_dict[d], steps))
		if(Goaled):
			print(tabs+"GOALED!!!!!!!!!!")

	def dismove(self, tabs):
		global TABLE
		(oldParent, newparent, d, Goaled) = self.stack[-1]
		newparent.isSitting = False
		newparent.child = None
		oldParent.isSitting = True
		oldParent.child = self
		self.parent = oldParent
		self.x = oldParent.i
		self.y = oldParent.j
		if Goaled:
			self.isLive = True
			newparent.isGoal = True
			newparent.isPlain = False
			newparent.name = "Goal"
		self.stack.pop()
		print("{}Butterfly{} UNDO \033[0;37;43m{}\033[0m".format(tabs,self.animalNumber, direction_dict[d]))

	def Contact(self):
		return self.name + "" + str(self.animalNumber)

	def __repr__(self):
		return self.Contact()

class Snail():
	def __init__(self, parent, i, j, animalNumber):
		self.parent = parent
		self.name = "Snail"
		self.animalNumber = animalNumber
		self.x = i
		self.y = j
		self.isLive = True
		self.stack = []

	def move(self, d, steps, tabs):
		global TABLE
		oldParent = self.parent
		oldParent.isSitting = False
		oldParent.child     = None
		i = oldParent.i
		j = oldParent.j
		if d == MOVE_UP:
			self.parent = TABLE[i-2][j] 
		if d == MOVE_DOWN:
			self.parent = TABLE[i+2][j] 
		if d == MOVE_LEFT:
			self.parent = TABLE[i][j-2] 
		if d == MOVE_RIGHT:
			self.parent = TABLE[i][j+2] 
		
		newparent = self.parent
		newparent.isSitting = True
		newparent.child     = self
		self.x = newparent.i
		self.y = newparent.j
		Goaled = False
		if newparent.isGoal:
			self.isLive = False
			newparent.isGoal = False
			newparent.isPlain = True
			newparent.name = "Plain"
			newparent.isSitting = False
			Goaled = True
		self.stack.append((oldParent, newparent, d, Goaled))

		print("{}Snail{} moved \033[0;37;42m{}\033[0m {}".format(tabs,self.animalNumber, direction_dict[d], steps))
		if(Goaled):
			print("{}GOALED!!!!!!!!!!".format(tabs))

	def dismove(self, tabs):
		global TABLE
		(oldParent, newparent, d, Goaled) = self.stack[-1]
		newparent.isSitting = False
		newparent.child = None
		oldParent.isSitting = True
		oldParent.child = self
		self.parent = oldParent
		self.x = oldParent.i
		self.y = oldParent.j
		if Goaled:
			self.isLive = True
			newparent.isGoal = True
			newparent.isPlain = False
			newparent.name = "Goal"
		self.stack.pop()
		print("{}Snail{} UNDO \033[0;37;43m{}\033[0m".format(tabs,self.animalNumber, direction_dict[d]))
	
	def __repr__(self):
		return self.Contact()

	def Contact(self):
		return self.name + "" + str(self.animalNumber)

class Dead(object):
	def __init__(self):
		self.name = "Dead"

class Node():
	def __init__(self, child, number, i, j, animalNumber):
		self.child = None

		# constant things for a node
		self.i = i
		self.j = j
		self.tag     = number
		self.isGoal  = False
		self.isDead  = False
		self.isPlain = False
		self.isSitting = False
		self.UP    = None
		self.DOWN  = None
		self.LEFT  = None
		self.RIGHT = None
		self.name  = None

		if child == GOAL:
			self.isGoal = True
			self.name = "Goal"
			GOALS.append(self)
		elif child == DEAD:
			self.isDead = True
			self.name = "Dead"
		elif child == PLAIN:
			self.isPlain = True
			self.name = "Plain"
		else:
			self.isPlain   = True
			self.isSitting = True
			if child == SPIDER:
				self.child = Spider(self, i, j, animalNumber)
				self.name  = "Spider"
			elif child == SNAIL:
				self.child = Snail(self, i, j, animalNumber)
				self.name  = "Snail"
			elif child == GRASSHOPPER:
				self.child = Grasshopper(self, i, j, animalNumber)
				self.name  = "Grasshopper"
			elif child == BUG:
				self.child = Bug(self, i, j, animalNumber)
				self.name  = "Bug"
			elif child == BEE:
				self.child = Bee(self, i, j, animalNumber)
				self.name  = "Bee"
			elif child == BUTTERFLY:
				self.child = Butterfly(self, i, j, animalNumber)
				self.name  = "Butterfly"
			else:
				raise Exception("Invalid Node {}".format(child))

			global ANIMALS
			ANIMALS.append(self.child)

	def nextNode(self, direction):
		if direction == MOVE_UP:
			return self.UP.UP
		elif direction == MOVE_DOWN:
			return self.DOWN.DOWN
		elif direction == MOVE_LEFT:
			return self.LEFT.LEFT
		elif direction == MOVE_RIGHT:
			return self.RIGHT.RIGHT
		else:
			raise Exception("Invalid node direction: {}".format(direction))

	def nextNodeType(self, direction):
		if self.nextNode(direction)!=None:
			if direction == MOVE_UP:
				return self.UP.UP.name
			elif direction == MOVE_DOWN:
				return self.DOWN.DOWN.name
			elif direction == MOVE_LEFT:
				return self.LEFT.LEFT.name
			elif direction == MOVE_RIGHT:
				return self.RIGHT.RIGHT.name
			else:
				raise Exception("Invalid node direction: {}".format(direction))
		else:
			return "Dead"

	def edge(self, direction):
		if direction == MOVE_UP:
			return self.UP
		elif direction == MOVE_DOWN:
			return self.DOWN
		elif direction == MOVE_LEFT:
			return self.LEFT
		elif direction == MOVE_RIGHT:
			return self.RIGHT
		else:
			raise Exception("Invalid edge direction: {}".format(direction))

	def edgeType(self, direction):
		if direction == MOVE_UP:
			return self.UP.name
		elif direction == MOVE_DOWN:
			return self.DOWN.name
		elif direction == MOVE_LEFT:
			return self.LEFT.name
		elif direction == MOVE_RIGHT:
			return self.RIGHT.name
		else:
			raise Exception("Invalid edgeType direction: {}".format(direction))

	def canMove(self, direction, tabs):
		# printAttrNode(self, tabs)
		# print("{}Checking... {}".format(tabs,self.child.Contact()))
		if self.isSitting == False:
			raise Exception ("Invalid node tested for movement!!")
		else:
			if self.child.name == "Snail":
				if self.child.isLive == False:
					return False, 0
				if (direction == MOVE_UP):
					if (self.UP.name!="Wall") and (self.UP.UP!=None) and (self.UP.UP.isSitting==False) and (self.UP.UP.isDead==False):
						return True, 1
					else:
						return False, 0
				if (direction == MOVE_DOWN):
					if (self.DOWN.name!="Wall") and (self.DOWN.DOWN!=None) and (self.DOWN.DOWN.isSitting==False) and (self.DOWN.DOWN.isDead==False):
						return True, 1
					else:
						return False, 0
				if (direction == MOVE_LEFT):
					if (self.LEFT.name!="Wall") and (self.LEFT.LEFT!=None) and (self.LEFT.LEFT.isSitting==False) and (self.LEFT.LEFT.isDead==False):
						return True, 1
					else:
						return False, 0
				if (direction == MOVE_RIGHT):
					if (self.RIGHT.name!="Wall") and (self.RIGHT.RIGHT!=None) and (self.RIGHT.RIGHT.isSitting==False) and (self.RIGHT.RIGHT.isDead==False):
						return True, 1
					else:
						return False, 0

			if self.child.name == "Spider":
				if self.child.isLive == False:
					return False, 0
				currP = self.child.parent
				steps = 0
				while True:
					if currP.edgeType(direction) == "Wall":
						print("{}Wall".format(tabs))
						break
					if currP.nextNodeType(direction) == "Dead":
						print("{}Dead".format(tabs))
						steps = 0
						break
					if currP.nextNode(direction).isSitting == True:
						print("{}someone is sitting, {}".format(tabs,currP.nextNode(direction).child))
						break
					steps+=1
					currP = currP.nextNode(direction)
				if steps!=0:
					return True, steps
				else:
					return False, 0

			if self.child.name == "Grasshopper":
				if self.child.isLive == False:
					return False, 0
				currP = self.child.parent
				steps = 0
				while True:
					# if currP.edgeType(direction) == "Wall":
					# 	print("{}Wall".format(tabs))
					# 	break
					if currP.nextNodeType(direction) == "Dead":
						print("{}Dead".format(tabs))
						steps = 0
						break
					if currP.nextNode(direction).isSitting == True:
						print("{}someone is sitting, {} JUMPING...".format(tabs,currP.nextNode(direction).child))
						# break
					else:
						steps+=1
						break
					steps+=1
					currP = currP.nextNode(direction)
				if steps!=0:
					return True, steps
				else:
					return False, 0

			if self.child.name == "Bug":
				if self.child.isLive == False:
					return False, 0
				currP = self.child.parent
				steps = 0
				looped = 0
				while True and looped<2:
					if currP.edgeType(direction) == "Wall":
						print("{}Wall".format(tabs))
						break
					if currP.nextNodeType(direction) == "Dead":
						print("{}Dead".format(tabs))
						steps = 0
						break
					if currP.nextNode(direction).isSitting == True:
						print("{}someone is sitting, {}".format(tabs,currP.nextNode(direction).child))
						break

					steps+=1
					currP = currP.nextNode(direction)
					looped += 1
				if steps!=0:
					return True, steps
				else:
					return False, 0
			
			if self.child.name == "Bee":
				if self.child.isLive == False:
					return False, 0
				currP = self.child.parent
				steps = 0
				# Skip step
				if currP.nextNode(direction) == None:
					return False, 0
				if currP.nextNode(direction).nextNode(direction) == None:
					return False, 0

				currP = currP.nextNode(direction)
				steps = 1
				while True:
					# if currP.edgeType(direction) == "Wall":
					# 	print("{}Wall".format(tabs))
					# 	break
					if currP.nextNodeType(direction) == "Dead":
						print("{}Dead".format(tabs))
						steps = 0
						break
					if currP.nextNode(direction).isSitting == True:
						print("{}someone is sitting, {} JUMPING...".format(tabs,currP.nextNode(direction).child))
						# break
					else:
						steps+=1
						break
					steps+=1
					currP = currP.nextNode(direction)
				if steps!=0:
					return True, steps
				else:
					return False, 0

			if self.child.name == "Butterfly":
				if self.child.isLive == False:
					return False, 0
				currP = self.child.parent
				steps = 0
				# Skip step
				if currP.nextNode(direction) == None:
					return False, 0
				if currP.nextNode(direction).nextNode(direction) == None:
					return False, 0
				if currP.nextNode(direction).nextNode(direction).nextNode(direction) == None:
					return False, 0

				currP = currP.nextNode(direction).nextNode(direction)
				steps = 2
				while True:
					# if currP.edgeType(direction) == "Wall":
					# 	print("{}Wall".format(tabs))
					# 	break
					if currP.nextNodeType(direction) == "Dead":
						print("{}Dead".format(tabs))
						steps = 0
						break
					if currP.nextNode(direction).isSitting == True:
						print("{}someone is sitting, {} JUMPING...".format(tabs,currP.nextNode(direction).child))
						# break
					else:
						steps+=1
						break
					steps+=1
					currP = currP.nextNode(direction)
				if steps!=0:
					return True, steps
				else:
					return False, 0

	def __repr__(self):
		if self.isSitting != False:
			return self.child.name
		elif self.isGoal == True:
			return "Goal"
		return "May be Animal"

	# def printNode():
	# 	# if self.boundaries[0].isWall :
	# 	if self.color == "RED":
	# 		print("{}\033[0;37;41m {} \033[0m".format(tabs,self.tag))
	# 	if self.color == "RED":
	# 		print("{}\033[0;37;41m {} \033[0m".format(tabs,self.tag))


def printAttrNode(n, tabs):
	attrs = vars(n)
	print(tabs+', '.join("%s: %s" % item for item in attrs.items()))

def printWorld():
	n = len(TABLE)
	m = len(TABLE[0])
	for i in range(n):
		for j in range(m):
			pass

class A():
	def __init__(self):
		self.count = 0
		self.right = None

class B():
	def __init__(self):
		self.count = 0

class C():
	def __init__(self):
		self.count = 0
		self.left = None

a = A()
b = B()
c = C()

a.right = b
c.left  = b
a.right.count += 1
c.left.count += 1

print(b.count)

d = b 
a.right.count += 1
c.left.count += 1
print(b.count)
print(d.count)
b.count+=10
print(b.count)
print(d.count)

# print(TABLE[0][0])
# print(vars(TABLE[0][0]))
# printAttrNode(TABLE[0][0])



# print("{}\033[0;37;40m Normal text\n")
# print("{}\033[2;37;40m Underlined text\033[0;37;40m \n")
# print("{}\033[1;37;40m Bright Colour\033[0;37;40m \n")
# print("{}\033[3;37;40m Negative Colour\033[0;37;40m \n")
# print("{}\033[5;37;40m Negative Colour\033[0;37;40m\n")
 
# print("{}\033[1;37;40m \033[2;37:40m TextColour BlackBackground          TextColour GreyBackground                WhiteText ColouredBackground\033[0;37;40m\n")
# print("{}\033[1;30;40m Dark Gray      \033[0m 1;30;40m            \033[0;30;47m Black      \033[0m 0;30;47m               \033[0;37;41m Black      \033[0m 0;37;41m")
# print("{}\033[1;31;40m Bright Red     \033[0m 1;31;40m            \033[0;31;47m Red        \033[0m 0;31;47m               \033[0;37;42m Black      \033[0m 0;37;42m")
# print("{}\033[1;32;40m Bright Green   \033[0m 1;32;40m            \033[0;32;47m Green      \033[0m 0;32;47m               \033[0;37;43m Black      \033[0m 0;37;43m")
# print("{}\033[1;33;40m Yellow         \033[0m 1;33;40m            \033[0;33;47m Brown      \033[0m 0;33;47m               \033[0;37;44m Black      \033[0m 0;37;44m")
# print("{}\033[1;34;40m Bright Blue    \033[0m 1;34;40m            \033[0;34;47m Blue       \033[0m 0;34;47m               \033[0;37;45m Black      \033[0m 0;37;45m")
# print("{}\033[1;35;40m Bright Magenta \033[0m 1;35;40m            \033[0;35;47m Magenta    \033[0m 0;35;47m               \033[0;37;46m Black      \033[0m 0;37;46m")
# print("{}\033[1;36;40m Bright Cyan    \033[0m 1;36;40m            \033[0;36;47m Cyan       \033[0m 0;36;47m               \033[0;37;47m Black      \033[0m 0;37;47m")
# print("{}\033[1;37;40m White          \033[0m 1;37;40m            \033[0;37;40m Light Grey \033[0m 0;37;40m               \033[0;37;48m Black      \033[0m 0;37;48m")

tabs = ""
INPUT = []
f = open("/home/vaibhav/Downloads/{}.csv".format(sys.argv[1]))
data = f.readlines()
for i in range(len(data)):
	if data[i][-1] == '\n':
		data[i] = data[i][:-1]
	line = data[i]
	chars = line.split(',')
	INPUT.append(chars)

print("{}Input looks like:".format(tabs))
print(DataFrame(INPUT))

###################################
TABLE = []
for i in range(len(INPUT)):
	row = [None]*len(INPUT[0])
	TABLE.append(row)

# print("{}Table looks like:".format(tabs))
# print(TABLE)
###################################
SIMPLE = 0 # .
WALL   = 1 # W
PLAIN  = 2 # n
SPIDER = 3 # S
SNAIL  = 4 # s
DEAD   = 5 # x
GOAL   = 6 # G
GRASSHOPPER = 7 # g
BUG    = 8 # b
BEE    = 9 # B
BUTTERFLY   = 10 # F

MOVE_UP = 100
MOVE_DOWN = 101
MOVE_LEFT = 102
MOVE_RIGHT = 103
direction_dict = {MOVE_UP: "UP", MOVE_DOWN: "DOWN", MOVE_LEFT:"LEFT", MOVE_RIGHT:"RIGHT" }


NodeNum = 0
ANIMALS = []
START_nodes = []
GOAL_nodes  = []
animalNumber = 0

for i in range(len(TABLE)):
	for j in range(len(TABLE[0])):
		if (INPUT[i][j]=='-'): 	# Useless
			continue
		elif (INPUT[i][j]=='.'):  # simple Edge
			TABLE[i][j]=Edge(SIMPLE, i, j)
		elif (INPUT[i][j]=='W'):  # Wall Edge
			TABLE[i][j]=Edge(WALL, i, j)
		else:
			if (INPUT[i][j]=='x'):  # Dead
				TABLE[i][j]=Node(DEAD, NodeNum, i, j, -1)
			elif (INPUT[i][j]=='G'):  # Goal
				TABLE[i][j]=Node(GOAL, NodeNum, i, j, -1)
				GOAL_nodes.append((TABLE[i][j], i, j))
			elif (INPUT[i][j]=='n'):  # Walkable Area
				TABLE[i][j]=Node(PLAIN, NodeNum, i, j, -1)
			else:
				if (INPUT[i][j]=='S'):  # Spider
					TABLE[i][j]=Node(SPIDER, NodeNum, i, j, animalNumber)
				elif (INPUT[i][j]=='s'):  # Snail
					TABLE[i][j]=Node(SNAIL, NodeNum, i, j, animalNumber)	
				elif (INPUT[i][j]=='g'):  # Grasshopper
					TABLE[i][j]=Node(GRASSHOPPER, NodeNum, i, j, animalNumber)
				elif (INPUT[i][j]=='b'):  # Bug
					TABLE[i][j]=Node(BUG, NodeNum, i, j, animalNumber)
				elif (INPUT[i][j]=='B'):  # Bee
					TABLE[i][j]=Node(BEE, NodeNum, i, j, animalNumber)
				elif (INPUT[i][j]=='F'):  # Butterfly
					TABLE[i][j]=Node(BUTTERFLY, NodeNum, i, j, animalNumber)
				else:
					raise Exception("Unknow entry in input file")
				START_nodes.append((TABLE[i][j], i, j))
				animalNumber += 1
			NodeNum += 1
			

print("Table looks like:")
print(TABLE)
###################################
# Adding edges to all nodes
# Edges are of the ordering: Left, Up, Right, Down
for i in range(len(TABLE)):
	for j in range(len(TABLE[0])):
		if ((i%2 ==1) and (j%2==1)):
			print(i, j)
			# printAttrNode(TABLE[i][j], "")
			TABLE[i][j].LEFT = TABLE[i][j-1]
			TABLE[i][j].UP = TABLE[i-1][j]
			TABLE[i][j].RIGHT = TABLE[i][j+1]
			TABLE[i][j].DOWN = TABLE[i+1][j]

# Adding nodes to all edges
for i in range(len(TABLE)):
	for j in range(len(TABLE[0])):
		if ((i%2 ==1) and (j%2==0)):
			TABLE[i][j].LEFT  = None if j==0 else TABLE[i][j-1] 
			TABLE[i][j].RIGHT = None if j==(len(TABLE[0])-1) else TABLE[i][j+1]

for i in range(len(TABLE)):
	for j in range(len(TABLE[0])):
		if ((i%2 ==0) and (j%2==1)):
			TABLE[i][j].UP   = None if i==0 else TABLE[i-1][j] 
			TABLE[i][j].DOWN = None if i==(len(TABLE)-1) else TABLE[i+1][j]
####################################
def CheckTableMaintainence():
	pass
	# global TABLE
	# for i in range(len(TABLE)):
	# 	for j in range(len(TABLE[0])):
	# 		if ((i%2 ==1) and (j%2==1)):
	# 			if(TABLE[i][j].isSitting)


def CheckAnimalMaintainence():
	for a in ANIMALS:
		if(a.isLive and a.parent.child.Contact() != a.Contact()):
			print(tabs + "ERROR: TYPE 1 for "+a.Contact() + " vs " + a.parent.child.Contact())
			return False
		elif a.parent.isSitting == False and a.isLive:
			print(tabs + "ERROR: animal's parent is marked as No one is sitting BUT animal is still LIVE")
			return False
		else:
			continue
	return True

MOVES = int(sys.argv[2])

print(len(START_nodes))
print(len(GOAL_nodes))


def AnimalsLeft():
	liveCount = 0
	for a in ANIMALS:
		if a.isLive == False:
			continue
		else:
			liveCount +=1
	return liveCount

def GoalsLeft():
	goalCount = 0
	for a in GOALS:
		if a.isGoal == True:
			goalCount += 1
	return goalCount

def dfs(moves_left, tillNow = "", tabs = ""):
	liveCount = 0
	for a in ANIMALS:
		if a.isLive == False:
			continue
		else:
			liveCount +=1
	# if(mo)
	if (liveCount == 0):
		return True

	# Early Prunning
	if (GoalsLeft()>moves_left):
		return False

	if (moves_left == 0):
		for a in ANIMALS:
			if a.isLive == True:
				print("{}\033[0;37;41m OUT OF MOVE \033[0m".format(tabs))
				return False
		return True
	# for animal in ANIMALS:
	# 	if (animal.Contact() != animal.parent.child.Contact()):
	# 		print(tabs + "ERROR: "+ animal.Contact())
	# 		raise Exception("ERROR")

	for animal in ANIMALS:
		for direction in [MOVE_UP, MOVE_RIGHT, MOVE_LEFT, MOVE_DOWN]:
			if (animal.isLive == False):
				continue
			# print("{}testing for.... {} {} : TESTED: {}".format(tabs, animal.Contact(), direction_dict[direction], animal.parent.child.Contact()))
			print(tabs + "Testing Animal = " + animal.Contact() + " direction: "+direction_dict[direction])
			#######
			# for a in ANIMALS:
			# 	if a.isLive:
			# 		print("{}{} LIVE: ({},{}) : sitting={}".format(a.Contact(), a.x, a.y, a.parent.isSitting))
			# 	else:
			# 		print("{}{} DEAD: ({},{}) : sitting={}".format(a.Contact(), a.x, a.y, a.parent.isSitting))
			# print("{}")
			#######
			# print("{} It is : {}".format(animal.parent.child.Contact()))
			t1, steps = animal.parent.canMove(direction, tabs)
			# print("{}Result: {},{}".format(tabs, t1, steps))
			if (t1):
				animal.move(direction, steps, tabs)
				assert(CheckAnimalMaintainence())
				# assert(CheckTableMaintainence())
				# assert(animal.Contact() == animal.parent.child.Contact())

				temptillNow = tillNow + " => {} {}({}->{})[{}]".format(animal.Contact(), direction_dict[direction], liveCount, AnimalsLeft(), steps)  
				t2 = dfs(moves_left-1, temptillNow, tabs+"\t")
				if t2:
					print("{}{} Success!!".format(tabs, temptillNow))	
					return True
				print("{}{} Failed".format(tabs, temptillNow))
				animal.dismove(tabs)
				print(tabs+"-------------------------")
				assert(animal.Contact() == animal.parent.child.Contact())
		print(tabs+"============= xxxxxxxx "+animal.Contact() + " xxxxxxxx =============\n")

	return False
	# (node, i, j) = s
	# for direction in [MOVE_UP, MOVE_RIGHT, MOVE_LEFT, MOVE_DOWN]:
	# 	canMove = node.can_move(direction)
	# 	if canMove:
	# 		ref.move


print("Starting....")
for s in START_nodes:
	(ref, i, j) = s
	print(ref, i, j)

for g in GOAL_nodes:
	(ref, i, j) = g
	print(ref, i, j)



ans = dfs(MOVES)
if (ans):
	print("Success")
else:
	print("Failed")

# isSuccess = False
# for s in START_nodes:
# 	isSuccess = 
# 	if isSuccess:
# 		print("{}Success")
# 		break

# if not isSuccess:
# 	print("{}Failed")

