def transpose(m):
    return map(list, zip(*m))
def matrix(m, n, e = None):
    return [[e]*n]*m
def Madd(a, b):
    return [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
def Msmult(m, c):
    return [[j*c for j in i] for i in m]
def rowreplace(m, row1, a, row2, b):
    rowI = [i*a for i in m[row1]]
    rowII = [i*b for i in m[row2]]
    m[row1] = [rowI[i] + rowII[i] for i in range(len(m[row2]))]
def hmatrix(m):
    pass
from fractions import Fraction

a = [[Fraction(i-j, 1) for i in range(3)] for j in range(2)]
print(a)
print(Madd(Msmult(a, Fraction(1, 3)), matrix(2, 3, 1)))

