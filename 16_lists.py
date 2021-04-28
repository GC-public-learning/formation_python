#coding:utf-8

""" lists
-------------------"""

# (arrays rarely used in python)

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

# browse a list with a range
for i in range(3):
	print(inventory[i])

print()
# acces 1 element from list
print(inventory[1])
print(inventory[-1]) # start from the end (! not indice)

# acces such number of elements from a list 
print(inventory[:2]) # 2 first
print(inventory[2:]) # 2 last

