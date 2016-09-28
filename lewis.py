class atom:
    def __init__(self, valence, final = 8):
        self.valence = valence
        self.unshared = valence
        self.final = final
        self.bonds = 0
    def formalcharge(self):
        return self.valence - self.unshared - self.bonds
    def isoctet(self):
        return 8 == self.unshared + self.bonds*2
    def bond(self, a):
        self.unshared -= 1
        self.bonds += 1
        a.unshared -= 1
        a.bonds += 1
##bond matrix:
##n = ['N', 'O', 'O']
##should be symetric and diagonal should be 0
##sum of row or columm is number of bonds
##  N  O  O
##N 0  1  2
##O 1  0  0
##O 2  0  0
H1 = atom(1, final = 2)
H2 = atom(1, final = 2)
H3 = atom(1, final = 2)
H4 = atom(1, final = 2)
C = atom(4)
N = atom(5)
P1 = atom(5)
P2 = atom(5)
P3 = atom(5)
P4 = atom(5)
S = atom(6)
O1 = atom(6)
O2 = atom(6)
O3 = atom(6)
#def lewis(molecule, charge): atoms = [valence 1, valence 2, ..., valence n]
charge = 0
molecule = [N, O1]
total = sum(i.valence for i in molecule) - charge
final = sum(i.final for i in molecule)
numbonds = (final - total)/2
if total % 2 == 1:
    print('free radical')
print(total, final, numbonds)
bonds = [0]*(len(molecule)*(len(molecule)-1)//2)

##try all bonds
##make sure pretty much all octets, or minimized octets, and connected
##print bonds

##for i in molecule:
##    try a bunch of bond combinations for just i and see which one works
##    if error, or reach end and not all octets, restart
##minimize, sum(abs(i.formalcharge()) for i in molecule), for lewis structure
