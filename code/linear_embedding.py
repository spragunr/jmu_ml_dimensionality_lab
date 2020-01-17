# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

X = np.random.random((100,2))

A = np.random.random((2,3))
A = A / np.linalg.norm(A, axis=0)
print(np.linalg.norm(A, axis=0))

Y = X.dot(A)
#print(Y)
plt.plot(Y[:,0], Y[:, 1], '*')
plt.show()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(Y[:,0], Y[:, 1], Y[:,2])
plt.show()
np.savetxt('embed.csv', Y, fmt='%.5f', delimiter=',')