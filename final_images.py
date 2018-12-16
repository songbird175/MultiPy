"""
A script for creating the images used in my linearity final
"""

import multipy as mp
import matplotlib.pyplot as plt
import numpy as np
from sympy import *

# #image 1, a scalar function
def example_scalar(x):
    return 2*x

scal = mp.ScalarFunc(example_scalar)
# scal.vis()

#image 2, a contour plot with the gradient
scal.contour()