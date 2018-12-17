"""
A script for creating the images used in my linearity final
"""

import multipy as mp
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from sympy.physics.vector import ReferenceFrame, curl

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

# #curl of a vector field
# R = ReferenceFrame('R')
# F = R[0]**2 * R[1] * R.x + R[1]*3 * R.y
# G = curl(F, R)

#image 13, a 2D curve
# curve1 = mp.VVF(Symbol('t')**3, 4*Symbol('t'))
# curve1.vis()

#image 14, a 3D curve
r_of_t = mp.VVF(cos(Symbol('t')), sin(Symbol('t')), Symbol('t'))
r_of_t.vis()