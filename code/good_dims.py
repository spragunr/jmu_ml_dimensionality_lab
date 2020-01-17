#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 09:18:20 2020

@author: spragunr
"""


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

num = 100

D = np.zeros((num, 6))
D[:,0] = np.random.randn(num)
D[:,1] = np.random.random(num) 
D[np.random.randint(num, size=25), 2] = .5
D[np.random.randint(num, size=25), 2] = 1.0
D[:,3] = np.random.randn(num)
D[:,4] = np.random.random(num) + .2 * D[:, 3]
D[:,5] =  D[:,1] * D[:,3]

print(D)


plt.plot(D[:,1], D[:,5], '*')
plt.plot(D[:,3], D[:,5], "o")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(D[:,1], D[:, 3], D[:,5])
plt.show()
np.savetxt('dims.csv', D, fmt='%.5f', delimiter=',')