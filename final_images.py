"""
A script for creating the images used in my linearity final
"""

import multipy as mp
import numpy as np
from sympy import *

#image 1, a scalar function
def example_func(x):
    return 2*x

a = mp.ScalarFunc(example_func)
a.vis()

#image 2, a contour plot with the gradient