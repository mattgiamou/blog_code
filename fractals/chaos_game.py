# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 20:27:44 2014

@author: Matt
"""

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import random as rnd

def get_regular_polygon(n):
    """ Returns 0-centered regular n-gon coordinates as complex array  
    """
    step = 2*np.pi/n
    theta = np.arange(0., n*step, step)
    complex_out = 1j*np.exp(1j*theta)
    return np.vstack([np.real(complex_out), np.imag(complex_out)])    
    
def chaos_game(polygon, seed, N, f):
    nDim = np.size(polygon, 0)
    nVerts = np.size(polygon, 1)
    fractal = np.zeros([nDim, N])
    current_point = seed
    for idx in xrange(0, N):
        ndx = rnd.randint(0, nVerts)
        vert = polygon[:, ndx]
        next_point = current_point + f*(vert-current_point)
        fractal[:,idx] = next_point
        current_point = next_point
    return fractal
    
    
seed_x = np.array([])

if __name__ == '__main__':
    n = 4
    N = int(1e4)
    f = 1.0/2.0
    seed = [0.5,0.5,0.5]
    #nGon = get_regular_polygon(n)
    nGon =  np.array([[0,1,1/2,1/2],
            [0,0,np.sqrt(3)/2, np.sqrt(3)/4],
            [0,0,0, np.sqrt(3)/2]]) 
    fractal = chaos_game(nGon, seed, N, f)
    
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    Axes3D.scatter(ax, fractal[0,:], fractal[1,:], fractal[2,:])
    plt.show()
    #plt.plot(fractal[0,:], fractal[1,:], 'b.')
    #plt.grid()
    #plt.show()