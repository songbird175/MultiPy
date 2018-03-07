"""
Code used for problem set 3. Code commented out so variable names could be re-used.
"""
import sys
sys.path.append('../')
import multipy as mp
import numpy as np
from sympy import *

#q10
# r_t = mp.VVF(sin(np.pi * Symbol('t')), Symbol('t'), cos(np.pi * Symbol('t')))
# r_t.vis()

#q18
# P = mp.Vector(-1, 2, 2)
# Q = mp.Vector(-3, 5, 1)
# PQ = mp.vector_sub(Q, P)
# print(PQ.x, PQ.y, PQ.z)
# r = mp.Parametric(P, PQ)
# print(r.r().x, r.r().y, r.r().z)
# print(r.eq_x, r.eq_y, r.eq_z)

#q21-26
# a = mp.VVF(Symbol('t') * cos(Symbol('t')), Symbol('t'), Symbol('t') * sin(Symbol('t')))
# a.vis(np.arange(0, 50, .2))
# b = mp.VVF(cos(Symbol('t')), sin(Symbol('t')), 1/(1 + Symbol('t')**2))
# b.vis()
# c = mp.VVF(Symbol('t'), 1/(1 + Symbol('t')**2), Symbol('t')**2)
# c.vis()
# d = mp.VVF(cos(Symbol('t')), sin(Symbol('t')), cos(2*Symbol('t')))
# d.vis()
# g = mp.VVF(cos(Symbol('t'))**2, sin(Symbol('t'))**2, Symbol('t'))
# g.vis()

#q7
# r_t = mp.VVF(4*sin(Symbol('t')), -2*cos(Symbol('t')))
# r_t.vis()
# t = (3*np.pi) / 4
# pos1 = r_t.pos_vector(t)
# rprime = mp.VVF(4*cos(Symbol('t')), 2*sin(Symbol('t')))
# rprime.pos_vector(t)

#q19
# r_t = mp.VVF(cos(Symbol('t')), 3*Symbol('t'), 2*sin(2*Symbol('t')))
# print(r_t.derivative())
# T = mp.VVF(-sin(Symbol('t')), 3, 4*cos(2*Symbol('t')))
# T.pos_vector(0)
# That = mp.Vector(0, 3, 4)
# print(That.direction().x, That.direction().y, That.direction().z)

#q23
# line1 = mp.VVF(Symbol('t')**2+1, 4*np.sqrt(Symbol('t')), np.exp(Symbol('t')**2 - Symbol('t')))
# print(line1.derivative())

#q5
# r_t = mp.VVF(3*cos(Symbol('t')), 2*sin(Symbol('t')))
# r_t.vis()
# vel = mp.VVF(-3*sin(Symbol('t')), 2*cos(Symbol('t')))
# vel.pos_vector(pi/3)
# acc = mp.VVF(-3*cos(Symbol('t')), -2*sin(Symbol('t')))
# acc.pos_vector(pi/3)