import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import scipy, math
import invtransamp as its

#Schrodinger cummulative distribution
def SCDF(x, n):
    return x - math.sin(2*n*math.pi*x)/(2*n*math.pi)

def sbox(nx, ny, nz, n = 1000):
    fig = plt.figure()
    ax = ax = fig.add_subplot(111, projection='3d')

    x = np.array(list(its.distrand(lambda i: SCDF(i, nx)) for c in range(n)))
    y = np.array(list(its.distrand(lambda i: SCDF(i, ny)) for c in range(n)))
    z = np.array(list(its.distrand(lambda i: SCDF(i, nz)) for c in range(n)))

    ax.scatter(x, y, z, c='r', marker='s')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()

sbox(1, 2, 3)
