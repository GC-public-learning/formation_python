#coding:utf-8

""" files
-------------------"""

""" opening mods
------------------
r : reading only
w : writing with replacing
a : writing on the end
x : reading and writing
r+: reading and wrinting in a same file
b : binary mode -> wb (writing with binary mode)
"""

# open (return TextIOWrapper type)
stream_animals = open("files/animals.txt", 'r')


""" READING
---------------"""

# read line (return string)
l1 = stream_animals.readline()
print(l1)
l2 = stream_animals.readline()
print(l2)

# read (return string)
# ! read() or readline() continue reading file from the last line readed !
content_stream_animals = stream_animals.read() 
print(content_stream_animals)

# browse word by word with such separator the string created just before
for s in content_stream_animals.split("\n"):
	print(s)

# change stream reading position, 
# 1st param = offset (1 offstet = 1 char)
# 2nd param = from which position (0 = start, 1 = current pos, 2 = end)
stream_animals.seek(0,0) # .seek(0) works 

# readlines (return list) continue reading after hold reading instructions
# ! carriage returns written too (\n)
list_lines_content_stream_animals = stream_animals.readlines()
print(list_lines_content_stream_animals)


# close (mandatory !)
stream_animals.close()
if stream_animals.closed: 
	print("{} closed".format(stream_animals.name))


# open file in structure (no need close() ! )
with open("files/animals.txt", 'r') as stream_animals_2:
	print(stream_animals_2.read())

# stream closed automaticaly on the end of the "with"
print(stream_animals_2.closed)


""" WRITING
---------------"""

with open("files/animals.txt", 'w') as stream_animals_3:
	# write (! crush all the file content)
	# mandatory writing carriage return "\n !"
	stream_animals_3.write("rat\n")
	stream_animals_3.write("cat\n")
	stream_animals_3.write("dog\n")
	stream_animals_3.write("elephant\n")



class Animal:
	# constructor
	def __init__(self, race, sort):
		self.sort = sort
		self.race = race

	# instance methods
	def show_attributes(self):
		print("race:{}, sort:{}".format(self.race, self.sort))


a1 = Animal("mouse", "mammal")
a2 = Animal("lizard", "reptile")
a3 = Animal("eagle", "bird")
a4 = Animal("ant", "insect")

a1.show_attributes()

import pickle

# write an object in binary mode with "pickle" library
# file automatically created if the file name doesn't exist !
with open("files/animals_binary", 'wb') as stream_animals:
	record = pickle.Pickler(stream_animals)
	record.dump(a1)
	record.dump(a2)
	record.dump(a3)
	record.dump(a4)

# read an object in binary mode with "pickle" library
with open("files/animals_binary", 'rb') as stream_animals:
	get_record = pickle.Unpickler(stream_animals)
	# load() works with offset like read methods !
	a1 = get_record.load()
	a2 = get_record.load()
	a3 = get_record.load()
	a4 = get_record.load()
	a1.show_attributes()
	a2.show_attributes()
	a3.show_attributes()
	a4.show_attributes()





