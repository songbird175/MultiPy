"""
A script for creating the images used in my linearity final
"""

import multipy as mp
import matplotlib.pyplot as plt
import numpy as np
from sympy import *

# #image 1, a scalar function
# def example_scalar(x):
#     return 2*x

# scal = mp.ScalarFunc(example_scalar)
# scal.vis()

# #image 2, a contour plot with the gradient
# scal.contour()

# #image 3, a 2D vector field
# def myX(x,y,z):
#     return x**2

# def myY(x,y,z):
#     return 3*y

# def myZ(x,y,z):
#     return 0

# vecf = mp.VectorField(myX, myY, myZ)
# vecf.vis()

# #image 4, a 3D vector field
# def myX(x,y,z):
#     return x

# def myY(x,y,z):
#     return y

# def myZ(x,y,z):
#     return z

# vecf = mp.VectorField(myX, myY, myZ)
# vecf.vis()