#coding:utf-8

""" heritage
-------------------"""

# mother class
class Vehicle:

	# constructor
	def __init__(self, label, speed):
		
		# object attributes
		self._label = label
		self._speed = speed
		self._position = 0

	# object methods

	def move(self, value):
		self._position += value


	# properties
	def _get_label(self):
		return self._label

	def _get_position(self):
		return self._position

	label = property(_get_label)
	position =property(_get_position)

# child class
class Car(Vehicle):

	# constructor
	def __init__(self, car_label, car_speed, nbr_doors):
		
		# mother class constructor
		Vehicle.__init__(self, car_label, car_speed)

		# object attributes
		self._nbr_doors = nbr_doors

	# object methods
	def active_wipers(self):
		print("wipers are activated")

	# overload mother methods
	def move(self, value):
		self._position += (3 * value)

# child class
class Plane(Vehicle):

	#constructor
	def __init__(self, plane_label, plane_speed, wingspan):
		
		# mother class constructor
		Vehicle.__init__(self, plane_label, plane_speed)

		# object attributes
		self._wingspan = wingspan

	# object methods

	# overload mother methods
	def move(self, value):
		self._position += (10 * value)


# child class
class Moto(Vehicle):
	pass

# multiple heritage is possible in python
class FlyingCar(Car, Plane):
	def __init__(self, label, speed, nbr_doors, wingspan):
		Car.__init__(self, label, speed, nbr_doors)
		Plane.__init__(self, label, speed, wingspan)


""" Main 
---------------"""

v1 = Vehicle("Toyota", 160)
v2 = Vehicle("F16", 2173)

c1 = Car("Toyota", 160, 4)
p1 = Plane("F16", 2173, 9.96)

# car
print("label:", c1.label)
print("position:", c1.position)
c1.move(1)
print("position:", c1.position)
c1.active_wipers()

# check instances and classes
print("object belongs Car class:", isinstance(c1, Car))
print("object belongs Plane class:", isinstance(c1, Plane))
print("class Car hinerit Vehicle class:", issubclass(Car, Vehicle))
print("class Vehicle hinerit Car class:", issubclass(Vehicle, Car))

# plane
print("\nlabel:", p1.label)
print("position:", p1.position)
p1.move(1)
print("position:", p1.position)

# flying car
fc1 = FlyingCar("super Car", 800, 4, 5)
print("\nlabel:", fc1.label)
print("position:", fc1.position)
fc1.move(1)
print("position:", fc1.position)
print("wingspan:", fc1._wingspan)
fc1.active_wipers()
print("object belongs Car class:", isinstance(fc1, Car))
print("object belongs Vehicle class:", isinstance(fc1, Vehicle))
print("object belongs Plane class:", isinstance(fc1, Plane))
