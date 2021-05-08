#coding:utf-8

""" asynchronous programming
--------------------------------""" 

import time
import threading


""" with functions
---------------------"""
def process_1():
	i = 0
	while i < 3:
		print(threading.currentThread())
		time.sleep(0.3)
		i += 1

def process_2():
	i = 0
	while i < 3:
		print(threading.currentThread())
		time.sleep(0.3)
		i += 1

# make objects Thread
th_1 = threading.Thread(process_1())
th_2 = threading.Thread(process_2())

# start multiple task
th_1.start()
th_2.start()

# block other operations until threads be finished
th_1.join()
th_2.join()



""" with child objects
------------------------"""

# make a lock for important instructions that gotta be executed alone
my_lock = threading.RLock()

class MyProcess(threading.Thread):
	def __init__(self, num):
		threading.Thread.__init__(self)
		self.num = num
	
	def run(self):
		# super().run() not needed beacause run is an empty  dedicated method
		# for developers who want to overload it in order to execute such
		# functions when the thread are started...
		i = 0
		while i < 3:

			# forbid others threads to be executed while 
			# these instructions are executed(threads are not necessarily 
			# executed in order !)
			with my_lock:
				print("thread {} : {}".format(self.num, 
					threading.currentThread()))
				time.sleep(0.3)
			i += 1

# childs objects Thread
pr_1 = MyProcess(1)
pr_2 = MyProcess(2)
pr_3 = MyProcess(3)

# starting multiple task
pr_1.start()
pr_2.start()
pr_3.start()

# block other operations until threads be finished
pr_1.join()
pr_2.join()
pr_3.join()

print("last operation")


