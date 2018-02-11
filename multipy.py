"""
Module for use in Multivariable Calculus
"""

import numpy as np
import multipy as mp
import mpmath
from sympy import *

class Vector:

    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.ihat = x * Symbol('i')
        self.jhat = y * Symbol('j')
        self.khat = z * Symbol('k')

    def magnitude(self):
        return np.sqrt(self.x**2 + self.y**2 + self.z**2)

    def direction(self):
        ihat_comp = self.x / self.magnitude()
        jhat_comp = self.y / self.magnitude()
        khat_comp = self.z / self.magnitude()
        return Vector(ihat_comp, jhat_comp, khat_comp)

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

def find_v(magnitude, theta):
    #finds the x & y components of a 2D vector w/ magnitude & theta relative to x-axis
    vsub1 = magnitude * np.cos(theta)
    vsub2 = magnitude * np.sin(theta)
    return Vector(vsub1, vsub2, 0)

def theta_between(v, w):
    #finds the angle theta between two vectors
    numer = mp.dot_prod(v, w)
    denom = v.magnitude() * w.magnitude()
    return acos(numer / denom)

def scal_project(v, w):
    #finds the scalar projection of v onto w
    return mp.dot_prod(v, w)/w.magnitude()

def projection_theta(v, theta):
    #finds the projection of v onto another vector separated by angle theta
    return (v.magnitude() * cos(theta))

def cross_prod(v, w):
    #cross product
    M = np.array([[v.x, v.y, v.z], [w.x, w.y, w.z]])
    for_i = M[:2, 1:3]
    for_j = np.array([M[:2, 0], M[:2, 2]])
    for_k = M[:2, :2]
    det_i = np.linalg.det(for_i)
    det_j = np.linalg.det(for_j)
    det_k = np.linalg.det(for_k)
    return (Symbol('i') * det_i) - (Symbol('j') * det_j) + (Symbol('k') * det_k)

