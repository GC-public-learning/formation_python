#coding:utf-8

""" dictionaries
-------------------"""

# helper
if False: help(dict)

# make dictionary
d1 = {}
d2 = {1: "one", 2: "two", "trois": 3, "dog": "Medor", (100,200): "tuple"}

# acces
print(d2)
print(d2[1]) # key and not index between "[]"
print(d2["trois"])


# add or change if element exists !
d2["quatre"] = 4
print(d2)


# remove
print(d2.pop("trois")) # pop() return the value removed at such key
del d2["quatre"]
print(d2)

# search key
print("dog" in d2)
print("Medor" in d2) # doesn't work with value 

# browsing
for k in d2:
	print(k)

for v in d2.values():
	print(v)

for k, v in d2.items():
	print((k, v)) # return tuple

# KeyError
try:
	print(d2[10])
except KeyError:
	print("Error, key notfound !")

# cloning 1st way
print("\ncloning"
	"\n---------------------")

d3 = d2.copy()
d3["dragon"] = "Elliott"
print(d2)
print(d3)

# cloning 2nd way
import copy
d4 = copy.deepcopy(d2)
d4["pooh bear"] = "Winnie"
print(d2)
print(d4)
print()

# functions with multiple named params (dictionary)
def function1(**params):
	# browse and print each key with its value of the dictionary "params" 
	for k, v in params.items():
		print((k, v))

	# print the dictionary "params" directly
	print("returned parameters:", params)

	return params # return dictionary

# ! as the keys are function params too, you can only name the keys with a name!
d5 = function1(name1 = "un", name2 = "Audi")
print(d5)



