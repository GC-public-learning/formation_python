#coding:utf-8

""" classes, attributes, constructor
--------------------------------------"""

# class
class Human:
	"""
	class for humans
	"""
	# class attributes (same value for all objects)
	# !! mandatory value assignment !!
	nbr_humans_created = 0

	# constructor
	def __init__(self, _name, _age = 1):
		print("human created in memory address ", self)

		# object attributes
		self.name = _name
		self.age = _age
		self.id = Human.nbr_humans_created+1
		Human.nbr_humans_created += 1

# object
h1 = Human("Jo", 37)
h2 = Human("Manu")
h3 = Human("Marc", 22)

# calling objects
print("name: {}\nage: {}\nid: {}\ntotal humans created: {}\n".format(h1.name, h1.age,h1.id, Human.nbr_humans_created))
print("name: {}\nage: {}\nid: {}\ntotal humans created: {}\n".format(h2.name, h2.age,h2.id, Human.nbr_humans_created))

# work with calling object to show class attribute..
print("name: {}\nage: {}\nid: {}\ntotal humans created: {}\n".format(h3.name, h3.age,h3.id, h3.nbr_humans_created)) 

#in python, no standard to make accessors but it's still possible ... ! 
#so this kind of handling is possible
h1.name = "Fred"
print("name: ", h1.name)