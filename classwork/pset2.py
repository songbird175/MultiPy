"""
My work on problem set 2 for Wellesley Math 205, Spring 2018
"""
import sys
sys.path.append('../')
import multipy as mp

#Section 12.3
#Q. 39
a_ = mp.Vector(-5, 12)
b_ = mp.Vector(4, 6)
scalar_projection = mp.scal_project(b_, a_)
vector_projection = mp.scalar_mult(a_.direction(), scalar_projection)

#Q. 49
r_ = mp.Vector((6-0), (12-10), (20-8))
F_ = mp.Vector(8, -6, 9)
W_ = mp.dot_prod(F_, r_) #answer in Joules

#Q. 50
F2_ = mp.find_v(1500, 30)
r2_ = mp.Vector(1000, 0, 0)
W2_ = mp.dot_prod(F2_, r2_) #answer in Joules

#Section 12.4
#Q. 3
a2_ = mp.Vector(2, 3, 0)
b2_ = mp.Vector(1, 0, 5)
cross_ab = mp.cross_prod(a2_, b2_)
#still need to verify that cross_ab is orthogonal (?)

#Q. 15
mag_u = 12
mag_v = 16
theta = 120
magnitude_crossuv = mp.cross_magnitude(mag_u, mag_v, theta)
#directed out of the page, per right hand rule

#Q. 19
u_ = mp.Vector(3, 2, 1)
v_ = mp.Vector(-1, 1, 0)
cross_uv = mp.cross_prod(u_, v_)
cross_vu = mp.cross_prod(v_, u_)
cross_uv_hat = cross_uv.direction()
cross_vu_hat = cross_vu.direction()

#Q. 27


#Q. 29


#Q. 33


#Q. 53


#Section 12.5
#Q. 3


#Q. 7


#Q. 19


#Q. 25


#Q. 31


#Q. 41


#Q. 59
