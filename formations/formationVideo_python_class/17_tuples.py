# -*- coding: utf-8 -*-

""" tuples
-------------------"""

# tuples
t1 = ()
t2 = (1,)
t3 = (1,2)
t4 = (3,4)
t5 = ("string", 1)

print(t1) 
print (t2)
print (t3)
print(t3[1])
print(t5)

# tuples are immutable container (like constants)
# t3[0] = 100 doesn't work !
# t1[0] = 12 doesn't work too even the tuple is empty

# on the other and reafectations still work with tuples
t3 = 100
print(t3)

# possible to make multiple assignments
nbr1, nbr2 = 1,2

# possible to make functions that return many elements
def get_position(t):
    return t[0], t[1]

v1, v2 = get_position(t4)
v1 = 1000
print(v1, v2)

t6 = get_position(t4)
# t6[0] = 100 doesn't work besause it's a tuple with this way


