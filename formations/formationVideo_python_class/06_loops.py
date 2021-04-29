#coding:utf-8

""" loops
-----------------"""

# os library to use a function to clear screen
import os

# while
# possible to use "break" to leave the loop
# possible to use "continue" to go back on the loop startup



flag = False
counter = 0

while not flag:
	#clear screen, posix for linux and mac, else for windows
	if os.name == "posix":
		os.system("clear")
	else : 
		os.system("cls")

	print("enter 1 to leave, attempt number ", counter + 1)
	word = input("> ")
	
	if word == "1":
		flag = True
	elif word =="0":
		continue
	if counter == 9:
		print("too many attempts (10 max)")
		break
	counter+=1

# for

#strings are recongnised as sequences
#end ='' prohibit carriage return
var = "hello world"
for c in var:
	print(c, end = '')
print()

# display01234
for i in range(5):
	print(i, end = '')
print()

# display 2345
for j in range(2, 6):
	print(j, end = '')
print()

# Increment the sequence with 3 (default is 1)
for x in range(2, 30, 3):
	print(x, end = '')
print()
