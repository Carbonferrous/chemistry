import math, random
#root find for cdf in range 0<x<1 CDF must be monotomicaly increasing
#basically a binary search for solution between [0, 1]
def rootfind(u, cdf, epsilon = .0001):
    x = .5
    i = 2
    while abs(cdf(x)-u)>epsilon:
        if cdf(x)<u:
            x += 1/2**i
        else:
            x -= 1/2**i
        i += 1
    return x
#returns a random number between [0, 1) which has the distribution
def distrand(cdf):
    return rootfind(random.random(), cdf)
