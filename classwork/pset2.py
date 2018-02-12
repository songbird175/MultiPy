"""
My work on problem set 2 for Wellesley Math 205, Spring 2018
"""
import sys
sys.path.append('../')
import multipy as mp
from sympy import *

#Section 12.3
#Q. 39
a_ = mp.Vector(-5, 12)
b_ = mp.Vector(4, 6)
scalar_projection = mp.scal_project(b_, a_)
vector_projection = mp.scalar_mult(a_.direction(), scalar_projection)
# print(a_.magnitude())
# print(mp.dot_prod(b_, a_))
# print(scalar_projection)
# print(a_.direction().ihat, a_.direction().jhat, a_.direction().khat)
# print(vector_projection.ihat, vector_projection.jhat, vector_projection.khat)

#Q. 49
r_ = mp.Vector((6-0), (12-10), (20-8))
F_ = mp.Vector(8, -6, 9)
W_ = mp.dot_prod(F_, r_) #answer in Joules
# print(W_)

#Q. 50
F2_ = mp.find_v(1500, 30)
r2_ = mp.Vector(1000, 0)
W2_ = mp.dot_prod(F2_, r2_) #answer in Joules
# print(F2_.ihat, F2_.jhat)
# print(W2_)

#Section 12.4
#Q. 3
a2_ = mp.Vector(2, 3, 0)
b2_ = mp.Vector(1, 0, 5)
cross_ab = mp.cross_prod(a2_, b2_)
# print(cross_ab.ihat, cross_ab.jhat, cross_ab.khat)
#cross_ab is orthogonal because the dot product of cross_ab and a2_ = the dot product of
#cross_ab and b2_ = 0
dot1 = mp.dot_prod(cross_ab, a2_)
dot2 = mp.dot_prod(cross_ab, b2_)
# print(dot1)
# print(dot2)

#Q. 15
mag_u = 12
mag_v = 16
theta = 120
magnitude_crossuv = mp.cross_magnitude(mag_u, mag_v, theta)
# print(magnitude_crossuv)
#directed out of the page, per right hand rule

#Q. 19
u_ = mp.Vector(3, 2, 1)
v_ = mp.Vector(-1, 1, 0)
cross_uv = mp.cross_prod(u_, v_)
cross_vu = mp.cross_prod(v_, u_)
# print(cross_uv.magnitude())
# print(cross_vu.magnitude())
# print(cross_uv.ihat, cross_uv.jhat, cross_uv.khat)
# print(cross_vu.ihat, cross_vu.jhat, cross_vu.khat)
cross_uv_hat = cross_uv.direction()
cross_vu_hat = cross_vu.direction()
# print(cross_uv_hat.ihat, cross_uv_hat.jhat, cross_uv_hat.khat)
# print(cross_vu_hat.ihat, cross_vu_hat.jhat, cross_vu_hat.khat)

#Q. 27
AB = mp.Vector((-1 - (-3)), (3-0))
AC = mp.Vector((5 - (-3)), (2-0))
cross_ABAC = mp.cross_prod(AB, AC)
# print(cross_ABAC.ihat, cross_ABAC.jhat, cross_ABAC.khat)
area = cross_ABAC.magnitude()
# print(area)

#Q. 29
#a)
PQ = mp.Vector((-2-1), (1-0), (3-1))
PR = mp.Vector((4-1), (2-0), (5-1))
nonzero_vector = mp.cross_prod(PQ, PR)
# print(nonzero_vector.ihat, nonzero_vector.jhat, nonzero_vector.khat)
#b)
# print(nonzero_vector.magnitude())
area_triangle = nonzero_vector.magnitude() / 2
# print(area_triangle)

#Q. 33
a1_ = mp.Vector(1,2,3)
b1_ = mp.Vector(-1,1,2)
c1_ = mp.Vector(2,1,4)
# print(mp.cross_prod(b1_, c1_).ihat, mp.cross_prod(b1_, c1_).jhat, mp.cross_prod(b1_, c1_).khat)
area_parallelepiped = mp.triple_scal_prod(a1_, b1_, c1_)
# print area_parallelepiped

#Q. 53
#explanation

#Section 12.5
#Q. 3
#Done on paper

#Q. 7
#Done on paper

#Q. 19
t = Symbol('t')
s = Symbol('s')
L1_ = mp.Vector((3 + 2*t), (4-t), (1 - 3*t))
L2_ = mp.Vector((1), (3 - 2*s), (4 + 5*s))
par = mp.is_mult(L1_, L2_)

#Q. 25
#Done on paper

#Q. 31
AB_ = mp.Vector(1, -1, 0)
AC_ = mp.Vector(1, 0, -1)
n_ = mp.cross_prod(AB_, AC_)

#Q. 41
#Done on paper

#Q. 59
n1_ = mp.Vector(5, -2, -2)
n2_ = mp.Vector(4, 1, 1)
v2_ = mp.cross_prod(n1_, n2_)