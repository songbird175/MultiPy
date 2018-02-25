"""
A script solely for testing
"""

import multipy as mp

r_ = mp.Vector(5,6,7)
rnaught = mp.Vector(1,2,3)
v_ = mp.Vector(2,0,4)
w_ = mp.Vector(10,12,14)
a_ = mp.Vector(8,9)
A = mp.Point(1, 2, 3)
B = mp.Point(4, 0, 2)
AB = mp.Vector(3, -2, -1)
paramAB = mp.Parametric(A, AB)

# print(paramAB.eq_x)

# print(paramAB.xy_intercept())
# print(paramAB.yz_intercept())
# print(paramAB.xz_intercept())

# print(paramAB.equations())
# print(paramAB.symmetric_x, paramAB.symmetric_y, paramAB.symmetric_z)

# print(r_.ihat, r_.jhat, r_.khat)

# print(r_.magnitude())

# print(rnaught.direction())

# print(mp.vector_add(r_, rnaught))
# print(mp.vector_sub(rnaught, v_))

# print(mp.scalar_mult(rnaught, 0))
# print(r_.magnitude() + v_.magnitude())

# print(mp.dot_prod(rnaught, v_))

# print(mp.is_mult(r_, w_))

# a_ = mp.find_v(5, 30)
# print(a_.khat)

# print(mp.theta_between(r_, rnaught))

# print(mp.projection(r_, rnaught))
# print(mp.projection_theta(r_, 30))

# print(mp.cross_prod(r_, a_))
# print(a_.z)