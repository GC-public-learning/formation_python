#coding:utf-8

""" variables
-----------------"""

# ust begin by a letter or underscore
age = 37
name = "jo"
txt = "My name is {} and i'm {} years old"

# show the type
print(type(age))

# format
print(txt.format(name,age))
print("My name is {} and i'm {} years old".format(name, age))

# f with {} 
print(f"Hello ! My name is {name} and i'm {age} years old")

# capture data, texte between () showed on the screen
age2 = input("enter age : ")
print("My name is {} and i'm {} years old".format(name, age))

# cast, change input string variable by a int or other...
age2 = int(age)
print("my age + 3 =", age2 + 3)
