# use some modules
import demo31_module

print("now in demo30")

demo31_module.foo(5, 6)
demo31_module.bar(7, 8)

import demo31_module as d31

d31.foo(9, 10)
d31.bar(11, 12)

from demo31_module import foo

foo(13, 14)

from demo31_module import bar as b

b(15, 16)

import numpy

x1 = numpy.array([1, 2, 3])
print(type(x1), x1)

import numpy as np

x2 = np.array([2, 3, 4])
print(type(x2), x2)

from numpy import array

x3 = array([7, 8, 9])
print(type(x3), x3)

print(x1 + x2 + x3)