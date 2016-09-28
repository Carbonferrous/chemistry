import math

e = 1.602*10**-19
me = 9.109*10**-31
e0 = 8.854*10**-12
h = 6.626*10**-34
c = 299792458

#Returns Energy at nth orbital of 1 electron atom of Z central charge / atom
def bohrE(n, Z):
    return -Z**2*e**4*me/(8*e0**2*n**2*h**2)
print('Last Ionization Energy of Atoms')
for Z in range(1, 11):
    print('{:d}: {:0.2f} eV/atom'.format(Z, bohrE(1, Z)*6.24*10**18))

spectra = []
for i in range(1, 100): #start n
    for j in range(i+1, 100):
        s = h*c*10**9/(bohrE(j, 1)-bohrE(i, 1))
        if 400 < s and s < 700:
            spectra += [s]
spectra.sort()

print('\nWavelengths of Emission Spectrum for Hydrogen')
for i in spectra:
    print('{:0.2f} nm'.format(i))
    
