'''def mul(mylist):
    result=1
    for x in mylist:
        result=result*x
    return result

lst1= [1,2,3]
lst2= [4,5,6]

print(mul(lst1))
print(mul(lst2))
'''
import numpy
import math
lst = [1,2,3]
lst2= [4,5,6]

r= numpy.prod(lst)
r1= math.prod(lst2)
print(r, r1)
'''

# Using Lambda
from functools import reduce
lst = [1,2,3]
lst2= [4,5,6]

r= reduce(lambda x,y: x*y, lst2)

print(r)
'''