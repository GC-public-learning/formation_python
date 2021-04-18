#coding:utf-8

""" conditions
-----------------"""

age = int(input("enter age : "))

# if, elif, else
# < > == <= >=
# !respect de indentation 1 tab in the if
if age == 0 :
	print("you aren't born")
elif age <= 20 :
	print("you are a young person")
else :
	print("you are an old person")

# operators in, not in
letter = 'a'
if letter in "ball":
	print("letter \"{}\" is in the word \"ball\"".format(letter))

# and, or
if letter in "ball" and age == 0:
	print("you've got the bonus message")

# interval with combination <
if 14 <= age <= 18:
	print("you are a teenager")
