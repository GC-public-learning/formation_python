#coding:utf-8

""" strings
-------------------"""

# explore the "str" class
if False: help(str)

s1 = "   hello world how are you !? " 

# all string methods work with a copy

# transform a string in uppercase
print(s1.upper())

# transform a string in lowercase
print(s1.lower())

# put an uppercase on the beginning of each string
print(s1.capitalize())

# put an uppercase on the beginning of each word
print(s1.title())

# fill the string on the beginning and the end with spaces to have 100 char total
print(s1.center(100))

# fill the string on the beginning and the end with "_" to have 100 char total
print(s1.center(100, '_'))

# return the index of the beginning of such string in an other string 
# return -1 if the string doesn't contain the last one
print(s1.find("world"))
print(s1.find("wagon"))

# return the index of the beginning of such string in an other string 
# return the exception "ValueError" if the string doesn't contain the last one
print(s1.index("world"))

try:
	print(s1.index("wagon"))
except ValueError:
	print ("Error ! the string doesn't containt such string")

# remove all useless spaces on the beginning and the end
print(s1.strip())

# replace such string by such string"
print(s1.replace("o", "z"))

# replace such string by such string (2 first occurrences)"
print(s1.replace("o", "z", 2))

# put all the word from a string into a list separate by such separator (a space here)
print(s1.split(" "))

# isalpha, isdigit, isdecimal, isnumeric, isalphanum
# is lower, isupper, isidentifier

# return "true" if the string is a reserved word
print("class".isidentifier())

# return true if a string belongs an other string
print("world" in s1)



