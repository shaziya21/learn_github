import math
x = math.sqrt(25)
print (x)
#for math fn we need to import it first

# floor = it will give the lower values
x = 9.6
print(math.floor(9.6))
print(math.ceil(9.6))


import math as m #whenever i have to use math i'll be using 'm'
print(math.sqrt(25))
print(m.sqrt(25))


#if we want to import only some functions
from math import sqrt,pow
print(pow(4,5))
help('math')
