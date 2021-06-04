"""
Case007: Copy data of a list to another list
"""
import copy
a = [1,2,3,4,['a','b']]
b = a
c = a[:]
d = copy.copy(a)
e = copy.deepcopy(a)
a.append(5)
a[4].append("c")

print(a)    #[1,2,3,4,['a','b','c'],5]
print(b)    #[1,2,3,4,['a','b','c'],5]
print(c)    #[1,2,3,4,['a','b','c']]
print(d)    #[1,2,3,4,['a','b','c']]
print(e)    #[1,2,3,4,['a','b']]
