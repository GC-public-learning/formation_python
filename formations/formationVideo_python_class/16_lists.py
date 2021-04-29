#coding:utf-8

""" lists
-------------------"""

# (arrays rarely used in python !)

# make a list
inventory = list()
inventory = []
inventory = [1, 2, "trois", 4]

# list with the same object many times
l = [2] * 10
l2 = ["tuc"] * 8

# list with a range of number
l3 = range(20)

# show the totality of the list
print(inventory[:])

print(inventory)
print(l2)
print(l3)

# browse a list with len(size) : not conventional
i = 0
while i < len(inventory):
	print(inventory[i])
	i+=1

# browse list with loop for
for value in inventory:
	print(value)

# browse a list with a range (last number excluded)
for i in range(len(inventory)):
	print(inventory[i])

# browse a list and make tuple with index for each element
for value in enumerate(inventory):
	print(value)

# browse a list and make tuple and separe index from element
for index, value in enumerate(inventory):
	print("index: {}, value: {}".format(index, value))


print()

# acces 1 element from list
print(inventory[1])
print(inventory[-1]) # start from the end (! not indice)

# acces such number of elements from a list 
print(inventory[:2]) # 2 first
print(inventory[2:]) # 2 last

# acces elements index 2 to index 4 (last element excluded !)
print(inventory[2:4])

# modify an element
inventory[2] = "tuc"
print(inventory[:])

# modify many elements
inventory[:2] = ["tic", "tic"]
print(inventory[:])
inventory[:2] = ["tac"] * 2
print(inventory[:])
inventory[:] = ["toc"] * len(inventory)
print(inventory)


# search
var = "toc"
if(var) in inventory:
	print("{} belongs the list".format(var))
else: print("\"{}\" doesn't belong the list".format(var))

# add an element at the end of the list
inventory.append("bim")
print(inventory)

# insert an element on such place
inventory.insert(1, "bam")
print(inventory)

#remove an element 
inventory.remove("bim") # with such name
del inventory[1] # with such index
print(inventory)

inventory = ["quatre", "bloc", "trois"]
print(inventory)

# sort list by alpha order or number (mix is forbidden !)
inventory.sort()
print(inventory)

# reverse all elements from list
inventory.reverse()
print(inventory)

# get the number of same elements
print(inventory.count("bloc"))

# effacer la liste
inventory.clear() # 1st way
inventory = [] # second way
print(inventory)


# make a list from a string with such separator(review chap 15)
s = "welcom to the world"
l = s.split(" ")
print(l[:])

# make a string from a list with such separator
# ! doesn't work with numbers
inventory = ["quatre", "bloc", "trois"]
print("_".join(inventory))

# make a clone
inventory2 = inventory # doesn't work (same memory adress)

import copy
inventory2 = copy.deepcopy(inventory2) # good way !
inventory2.append("zoom")
print(inventory)
print(inventory2)

# concatenate 2 list
inventory += inventory2
print(inventory)
inventory.extend(inventory2)
print(inventory)

