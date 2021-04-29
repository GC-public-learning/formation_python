#coding:utf-8

def speak(person = "jo", message = "hi"):
	print("{} : {}".format(person, message))

def sum(num1, num2):
	print("{} + {} = {}".format(num1, num2, num1 + num2))

# test
# if python interpeter execute this code from this file
# file "lib1.py" to execute in the console or shell with python3 instruction
if __name__ == "__main__":
	speak()
	speak(message = "good by")
	sum(4, 5)