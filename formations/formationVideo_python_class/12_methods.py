#coding:utf-8

""" methods
-------------"""

class Car: 
	""" class for cars """
	
	# class attributes
	total_cars = 0

	# constructor
	def __init__(self, label):
		
		#object attributes
		self.label = label
		self.id = Car.total_cars + 1
		self.started = False
		self.speed = 0
		Car.total_cars += 1

		print("car {} created".format(self.id))

	# object methods
	def start(self, started):
		self.started = started

	def accelerate(self):
		self.speed += 1

	def print_state(self):
		print("car {}\n-----------".format(self.id))
		print("label:", self.label)
		print("started:", self.started )
		print("speed:", self.speed)
		print("")

	# class methods
	def change_total_cars(cls, total_cars):
		Car.total_cars = total_cars

	# prevent python to use such method as class method
	change_total_cars = classmethod(change_total_cars)

	# static methods
	def print_hello():
		print("Hello !")

	# prevent python to use such method as static method
	print_hello = staticmethod(print_hello)


c1 = Car("Toyota")
c2 = Car("BMW")

c1.started = True
c1.accelerate()
c1.print_state()

c2.print_state()

print("total cars created:", Car.total_cars)
Car.change_total_cars(8)
print("total cars created:", Car.total_cars)

Car.print_hello()

