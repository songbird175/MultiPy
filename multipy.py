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
    sum_ihat = v.ihat + w.ihat
    sum_jhat = v.jhat + w.jhat
    sum_khat = v.khat + w.khat
    return (sum_ihat, sum_jhat, sum_khat)

def vector_sub(v, w):
    diff_ihat = v.ihat - w.ihat
    diff_jhat = v.jhat - w.jhat
    diff_khat = v.khat - w.khat
    return (diff_ihat, diff_jhat, diff_khat)