#coding:utf-8

""" exceptions
-----------------"""

number = input("enter a number : ")

# try, except, else, finally
try:
	number = int(number)
	number = (number) / number
except:
	print("Error, number only !")
else:
	print("number is", number)
finally:
	print("end")

""" target a kind of exception
ValueError, 
NameError, 
TypeError, 
ZeroDivisionError, 
OSError, 
AssertionError """
number = input("enter a number : ")

try:
	number = int(number)
	number2 = number / number
	assert number < 100
except ZeroDivisionError:
	print("Error, number other than 0 !")
except ValueError:
	print("Error, number only !")
except AssertionError:
	print("Error, number can't be above 100")
except:
	print("Unknown error")
else:
	print("number / number = ", number2)
finally:
	print("end")

print("number = ",number)


# personal exception
if number == 8:
		raise ZeroDivisionError("Error 8 isn't possible !")

