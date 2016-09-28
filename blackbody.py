import math, scipy
import numpy as np
import matplotlib.pyplot as plt

#Constants
kb = 1.38064852*10**-23 #J/K
c = 299792458 #m/s
h = 6.62607004*10**-34 #Js

def planck(l, T):
    l = l*10**-9 #convert from nm to m
    return 2*h*c**2/(l**5*np.expm1(h*c/(l*kb*T)))

def dispplank(T = 5250, minimum = 10, maximum = 2500):
#   dispplank(T = K   , minimum = nm, maximum = nm  ):
    w = np.arange(minimum, maximum, 10)
    p = planck(w, T)*10**-13
    wmax = .2*h*c/(kb*T)
    print('Max intensity at: {:0.2f} nm'.format(wmax*10**9))
    plt.plot(w, p)
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Intensity (some unit)')
    plt.show()
    return

dispplank()
