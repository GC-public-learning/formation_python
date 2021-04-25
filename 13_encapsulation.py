#coding:utf-8

""" encapsulation
-------------------"""

class Car:
	""" class for cars """
	def __init__(self, label):
		self._label = label

	# property (getter, setter, deleter, helper)
	def _get_label(self):
		try:
			return self._label
		except AttributeError:
			print("attribut \"label\" doesn't exist")

	def _set_label(self, label):
		if label == "":
			self._label = "xxx"
		else: self._label = label

	def _del_label(self):
		del self._label

	# prevent python to use such method as property
	label = property(_get_label, _set_label, _del_label, "i'm a label")



# main
c1 = Car("Ford")
print(c1.label)

c1.label = input("enter new label: ")
print(c1.label)

l = c1.label
print("l:", l)

del c1.label
l = c1.label
print("l:", l)

# help: show some infos of concerned class
help(Car)
help(Car.label)

