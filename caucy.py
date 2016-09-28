import math, scipy
import numpy as np
import matplotlib.pyplot as plt
import random

#Cauchy Distribution
def cauchy(x, x0, fwhm, I):
    return I*fwhm**2/((x-x0)**2+fwhm**2)
#Sum of Cauchy Distributions
def cauchysum(x, points):
    #points is a list of tuples containing (center, full width half maxima, scale)
    return sum(cauchy(x, x0, fwhm, I) for x0, fwhm, I in points)

#Find Peaks, FWHM, and intensity
##Program Details:
##Smooth and Denoise Data
##Identify # of Maxima
##Find maxima locations(x0)
##Find intensity for each maxima
##Find Shape perameter
##Recursivly Reajust shape/intensity for each curve t
##    account for other curves until detail is satisfied,
##    make sure doesn't jump around in reducing the thing
##Restrictions:
##    can't find 2 curves which seem to blend together
##    The closer the maxima are, the larger the intensity and/or the larger the shape parameter
##    if abs(x0[i] - x0[j])/(I[i]*fwhm[i]+I[j]*fwhm[j]) < epsilon: error

def cauchymatch(data):
    return [(7000, 700, 2), (9000, 500, 5)]

x = np.arange(4000, 14000, 100)
#Make Fake Data
data = cauchysum(x, [(7000, 700, 2), (9000, 500, 5)]) + np.random.normal(0, .1, len(x))

#Calculate points using magic formula
predicted = cauchymatch(data)
y1 = cauchysum(x, predicted)

#Display Results
print(predicted)
plt.plot(x, data, 'bs', x, y1)
plt.xlabel('Wavenumber')
plt.ylabel('Intensity')
plt.show()
