#coding:utf-8

""" functions
-----------------"""

"""convention :
- no space before :
- snake_case for variables and functions
- CamelCase for classes and exceptions
- see "https://python.sdv.univ-paris-diderot.fr/15_bonnes_pratiques/" for other rules (french)

"""

# def
def hello_word():
	print("hello word")

hello_word()

# def with params
def hello_word_params(name, message):
	print("hello {} {}".format(name, message))

hello_word_params("jo","how are you ?")


# otional params
def hello_word_params2(name, message = "cool"):
	print("hello {} {}".format(name, message))

hello_word_params2("ben")

"""
! an optional param doesn't need to be written only if all the params after are described or if this last one is the only one
	def hello_word_params2(name="jo", message):
	print("hello {} {}".format(name, message))
	DOESN'T WORK !! """



# possible to cast params to put them in any order
def hello_word_params3(name = "jo", message = "cool"):
	print("hello {} {}".format(name, message))

hello_word_params3(message = "bingo", name = "jojo")

# enter an unknown number of params, '*'' is not a pointer !
def show_some_items(*items):
	for i in items:
		print(i)

show_some_items("bingo", 2, True)


# soverloading ?
# overloading doesn't work in python, the last function replace the function before..

def show_something(thing):
	print("item : ", thing)
def show_something(thing, thing2):
	print("items : ", thing, thing2)

# show_something("car") -->doesn't work 
# because this function is replaced by the last one that take 2 arguments

# that works
show_something(5, True)


#return
num1 = 2
num2 = 5

def calcul_sum(num1, num2):
	return num1 + num2

print("sum of {} and {} = {}".format(num1, num2, calcul_sum(num1, num2)))






