"""
Code used for problem set 3
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

#q50
# r1 = mp.VVF(Symbol('t'), Symbol('t')**2, Symbol('t')**3)
# r2 = mp.VVF(1+2*Symbol('t'), 1+6*Symbol('t'), 1+14*Symbol('t'))
# r1.vis()
# r2.vis()