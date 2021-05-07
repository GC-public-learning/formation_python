#coding:utf-8

""" dates handling
------------------------""" 

# object handling with datetime library

from datetime import *

d1 = datetime(2021, 5, 7, 4, 20, 34) # date+ time
d2 = datetime(2021, 5, 7, 4, 20, 33)
d3 = date(2021, 5, 7) # date
d4 = time(4, 31, 30) # time


# overloading handled
if d1 > d2:
	print("{} is bigger than {}".format(d1, d2))
elif d1 < d2:
	print("{} is smaller than {}".format(d1, d2))
else:
	print("{} is equal than {}".format(d1, d2))


# get 1 only element
print(d1.year)

# actual datetime (with microseconds !)
print(datetime.now())

# actual day
print(date.today())

# actual time (time.now() doesn't exist -> need to be personalised)
print("{}:{}".format(datetime.now().hour, datetime.now().minute))