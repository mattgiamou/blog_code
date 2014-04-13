# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 21:03:20 2014

@author: Owner
"""
import numpy as np
from matplotlib import pyplot as plt
from scipy import random as rnd

class Affine:
    A = np.array([[1.0, 0],
                  [0.0, 1.0]])
    b = np.array([0.0, 0.0])
    
    def __init__(self, A, b):
        self.A = A
        self.b = b
        
    def transform(self, x):
        return np.dot(self.A,x) + self.b
        
def rand_cdf(cdf):
    N = len(cdf)
    v = rnd.rand()
    for idx in xrange(0,N):
        if v <= cdf[idx]:
            return idx
        
def fern_fractal(F, cdf, N):

    x0 = np.array([0.0, 0.0])
    fractal = np.zeros([2, N])
    
    for idx in xrange(0,N):
        ndx = rand_cdf(cdf)
        f = F[ndx]
        x1 = f.transform(x0)
        fractal[:,idx] = x1
        #x0 = fractal[:, rnd.randint(0,idx+1)]
        x0 = x1
    return fractal
        
F = []
P = [0.01, 0.85, 0.07, 0.07]
cdf = np.cumsum(P)

A1 = np.array([[0.0, 0.0],
               [0.0, 0.16]])
b1 = np.array([0.0, 0.0])
F.append(Affine(A1, b1))

A2 = np.array([[0.85, 0.04],
               [-0.04, 0.85]])
b2 = np.array([0.0, 1.6])
F.append(Affine(A2, b2))

A3 = np.array([[0.2, -0.26],
               [0.23, 0.22]])
b3 = np.array([0.0, 1.6])
F.append(Affine(A3, b3))

A4 = np.array([[-0.15, 0.28],
               [0.26, 0.24]])
b4 = np.array([0.0, 0.44])
F.append(Affine(A4, b4))
    
if __name__ == '__main__':
    
    N = int(5e5)
    fract = fern_fractal(F, cdf, N)
    plt.figure()
    plt.grid()
    plt.scatter(fract[0,:],fract[1,:], s=0.08, facecolor='0.5', lw = 0)
    plt.show()
