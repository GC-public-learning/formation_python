#coding:utf-8

""" modularity
-----------------"""

#import module(file)
import math
print(math.sqrt(100))

#import function from module
from math import sqrt
print(sqrt(100))

#os.system -> execute shell commands
import os
os.system("python3 7_functions.py")

# create and import your own module
# pycache file created automatically since python3
import modules.module1
modules.module1.speak()
modules.module1.sum(2,8)

# make calling module shorter
import modules.module1 as module1
module1.speak()
module1.sum(5,3)