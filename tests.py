"""
A script solely for testing
"""

from multipy import Vector

r_ = Vector(5,6,7)

print(r_.ihat, r_.jhat, r_.khat)

print(r_.magnitude())

print(r_.direction())