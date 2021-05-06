#coding:utf-8

""" time handling
------------------------"""

from time import *

# sleep (s)
sleep(1)

# start date = january 1st 1970
# time since this date (s) (timestamp)
print(time())

# current time in structure
print(localtime())

# recover the timestamp from the localtime
print(mktime(localtime()))


# use
begin = time()
counter = 0

# loop's working while such time
while time() < begin + 3:
	print(counter)
	sleep(1)
	counter+=1


"""
strftime
---------------
%Y : years (4 digits)
%y : years (2 digits)
%m : months
%a : weekday abbreviated
%A : weekday full
%b : month name abbreviated
%B : month name full
%d : days of the month
%j : days of the year
%H : hours (24)
%I : hours (12)
%M : minutes
%S : seconds
%p : AM/PM
%Z : timezone

"""
print(strftime("%a %b %d %y %I:%M %p")) # Thu May 06 21 07:48 PM


