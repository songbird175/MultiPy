"""
Module for use in Multivariable Calculus
"""

import numpy as np
import multipy as mp
import mpmath
import seaborn
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import *

class Point:

    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

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

    def scalar_mult(self, n):
    #scalar multiplication
        scal_ihat = self.x * n
        scal_jhat = self.y * n
        scal_khat = self.z * n
        return Vector(scal_ihat, scal_jhat, scal_khat)

    def is_mult(self, w):
        #checks if two vectors are scalar multiples of each other (parallel)
        if self.ihat / w.ihat == self.jhat / w.jhat and self.ihat / w.ihat == self.khat / w.khat:
            return True
        else:
            return False

    def projection_theta(self, theta):
        #finds the projection onto another vector separated by angle theta
        return (self.magnitude() * np.cos(theta))

class Parametric:

    def __init__(self, rnaught, v, t=Symbol('t')):
        self.rnaught = rnaught
        self.direction = v
        self.t = t

        self.symmetric_x = (Symbol('x') - rnaught.x) / v.x
        self.symmetric_y = (Symbol('y') - rnaught.y) / v.y
        self.symmetric_z = (Symbol('z') - rnaught.z) / v.z

        self.eq_x = self.rnaught.x + (self.direction.x * self.t)
        self.eq_y = self.rnaught.y + (self.direction.y * self.t)
        self.eq_z = self.rnaught.z + (self.direction.z * self.t)

    def xy_intercept(self):
        x = self.direction.x * (-self.rnaught.z / self.direction.z) + self.rnaught.x
        y = self.direction.y * (-self.rnaught.z / self.direction.z) + self.rnaught.y
        return (x, y)

    def yz_intercept(self):
        y = self.direction.y * (-self.rnaught.x / self.direction.x) + self.rnaught.y
        z = self.direction.z * (-self.rnaught.x / self.direction.x) + self.rnaught.z
        return (y, z)

    def xz_intercept(self):
        x = self.direction.x * (-self.rnaught.y / self.direction.y) + self.rnaught.x
        z = self.direction.z * (-self.rnaught.y / self.direction.y) + self.rnaught.z
        return (x, z)

    def r(self):
        return mp.Vector(self.eq_x, self.eq_y, self.eq_z)

class Plane:

    def __init__(self, rnaught, n):
        self.rnaught = rnaught
        self.n = n
        self.x = Symbol('x')
        self.y = Symbol('y')
        self.z = Symbol('z')
        self.gen_eq = self.equations(self.x, self.y, self.z)

    def equations(self, x, y, z):
        x_comp = self.n.x*(x-self.rnaught.x)
        y_comp = self.n.y*(y-self.rnaught.y)
        z_comp = self.n.z*(z-self.rnaught.z)
        return x_comp + y_comp + z_comp

    def x_intercept(self):
        numer = (self.n.y * self.rnaught.y) + (self.n.z * self.rnaught.z)
        return (numer / self.n.x) + self.rnaught.x

    def y_intercept(self):
        numer = (self.n.x * self.rnaught.x) + (self.n.z * self.rnaught.z)
        return (numer / self.n.y) + self.rnaught.y

    def z_intercept(self):
        numer = (self.n.y * self.rnaught.y) + (self.n.x * self.rnaught.x)
        return (numer / self.n.z) + self.rnaught.z

class VVF:

    def __init__(self, i, j, k=0):
        self.t = Symbol('t')
        self.h = Symbol('h')
        self.x = sympify(i)
        self.y = sympify(j)
        self.z = sympify(k)
        self.eq = self.x + self.y + self.z
        self.ihat = i * Symbol('i')
        self.jhat = j * Symbol('j')
        self.khat = k * Symbol('k')

    def vis(self, domain=np.arange(-10,10,0.02)):
        xs, ys, zs = np.zeros(len(domain)), np.zeros(len(domain)), np.zeros(len(domain))
        pos = 0
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        for num in domain:
            xs[pos] = self.x.evalf(subs={self.t:num})
            ys[pos] = self.y.evalf(subs={self.t:num})
            zs[pos] = self.z.evalf(subs={self.t:num})
            pos += 1
        ax.plot(xs, ys, zs)
        return plt.show()

    def continuous(self, a):
        mylim = limit(self.eq, self.t, a)
        ev = self.eq.evalf(subs={self.t:a})
        if ev == mylim:
            return True, mylim
        else:
            return False, mylim, ev

    def derivative(self):
        r = self.eq
        rh = self.eq.subs(self.t, (self.t + self.h))
        return limit((rh - r) / self.h, self.h, 0)

    def pos_vector(self, t):
        xpos = [self.x.subs(self.t, t)]
        ypos = [self.y.subs(self.t, t)]
        zpos = [self.z.subs(self.t, t)]
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlim(0, 5)
        ax.set_ylim(0, 5)
        ax.set_zlim(0, 5)
        ax.quiver([0], [0], [0], xpos, ypos, zpos, pivot='tail')
        plt.show()
        return mp.Vector(xpos[0], ypos[0], zpos[0])

def vector_add(v, w):
    #vector addition
    sum_ihat = v.x + w.x
    sum_jhat = v.y + w.y
    sum_khat = v.z + w.z
    return Vector(sum_ihat, sum_jhat, sum_khat)

def vector_sub(v, w):
    #vector subtraction
    diff_ihat = v.x - w.x
    diff_jhat = v.y - w.y
    diff_khat = v.z - w.z
    return Vector(diff_ihat, diff_jhat, diff_khat)

def dot_prod(v, w):
    #dot product
    dot_i = v.x * w.x
    dot_j = v.y * w.y
    dot_k = v.z * w.z
    return dot_i + dot_j + dot_k

def find_v(magnitude, theta):
    #finds the x & y components of a 2D vector w/ magnitude & theta relative to x-axis
    vsub1 = magnitude * np.cos(theta)
    vsub2 = magnitude * np.sin(theta)
    return Vector(vsub1, vsub2)

def theta_between(v, w):
    #finds the angle theta between two vectors
    numer = mp.dot_prod(v, w)
    denom = v.magnitude() * w.magnitude()
    return acos(numer / denom)

def scal_project(v, w):
    #finds the scalar projection of v onto w
    return mp.dot_prod(v, w)/w.magnitude()

def cross_prod(v, w):
    #cross product
    M = np.array([[v.x, v.y, v.z], [w.x, w.y, w.z]])
    for_i = M[:2, 1:3]
    for_j = np.array([M[:2, 0], M[:2, 2]])
    for_k = M[:2, :2]
    det_i = np.linalg.det(for_i)
    det_j = np.linalg.det(for_j)
    det_k = np.linalg.det(for_k)
    return Vector(det_i, -det_j, det_k)

def cross_magnitude(m, n, theta):
    #magnitude of the cross product
    return m * n * sin(theta)

def triple_scal_prod(u, v, w):
    #triple scalar product
    cross = mp.cross_prod(v, w)
    return mp.dot_prod(u, cross)

def position_vector(rnaught, v, t):
    #finds the position vector given initial point, direction vector, & time t
    tv = mp.scalar_mult(v, t)
    return mp.vector_add(rnaught, tv)