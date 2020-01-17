#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 16:30:11 2020
https://stackoverflow.com/questions/6802577/rotation-of-3d-vector
@author: spragunr
"""
import numpy as np
from numpy import cross, eye, dot
from scipy.linalg import expm, norm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def M(axis, theta):
    return expm(cross(eye(3), axis/norm(axis)*theta))

v, axis, theta = [3,5,0], [4,4,1], 1.2
M0 = M(axis, theta)
print(np.linalg.norm(v))
print(np.linalg.norm(dot(M0,v)))

# [ 2.74911638  4.77180932  1.91629719]
cur = np.array([0.,0.,0.])
vel = np.array([1.,1.,1.])


points = []
for i in range(400):
    cur = cur + .01 * vel
    axis = np.random.random(3) -.5
    theta = 1 * np.random.random()
    vel = M(axis,theta).dot(vel)
    points.append(cur)
 
    

points = np.array(points)
np.random.shuffle(points)
print(points)
plt.plot(points[:,0], points[:,1], '*')
plt.show()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:,0], points[:, 1], points[:,2])
plt.show()
np.savetxt('manifold.csv', points, fmt='%.5f', delimiter=',')