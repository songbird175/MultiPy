"""
Module for use in Multivariable Calculus
"""

import numpy as np
from sympy import *

class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.ihat = x * Symbol('i')
        self.jhat = y * Symbol('j')
        self.khat = z * Symbol('k')

    def magnitude(self):
        return (self.x + self.y + self.z)

    def direction(self):
        ihat_comp = self.ihat / self.magnitude()
        jhat_comp = self.jhat / self.magnitude()
        khat_comp = self.khat / self.magnitude()
        return (ihat_comp, jhat_comp, khat_comp)

def vector_add(v, w):
    #vector addition
    sum_ihat = v.ihat + w.ihat
    sum_jhat = v.jhat + w.jhat
    sum_khat = v.khat + w.khat
    return (sum_ihat, sum_jhat, sum_khat)

def vector_sub(v, w):
    #vector subtraction
    diff_ihat = v.ihat - w.ihat
    diff_jhat = v.jhat - w.jhat
    diff_khat = v.khat - w.khat
    return (diff_ihat, diff_jhat, diff_khat)

def scalar_mult(v, n):
    #scalar multiplication
    scal_ihat = v.ihat * n
    scal_jhat = v.jhat * n
    scal_khat = v.khat * n
    return (scal_ihat, scal_jhat, scal_khat)

def dot_prod(v, w):
    #dot product
    dot_i = v.x * w.x
    dot_j = v.y * w.y
    dot_k = v.z * w.z
    return (dot_i + dot_j + dot_k)

def is_mult(v, w):
    #checks if two vectors are scalar multiples of each other (parallel)
    if v.ihat / w.ihat == v.jhat / w.jhat and v.ihat / w.ihat == v.khat / w.khat:
        return True
    else:
        return False

