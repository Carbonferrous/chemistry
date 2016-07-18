import re

elements = {}
f = open('elements.txt')
z = 1
for line in f:
    symbol, name, mass = line.strip().split(' ')
    mass = float(mass)
    elements[symbol] = mass
    z += 1
#print(elements)

def massHelper(molecule):
    m = 0
    for e in re.findall('[A-Z][a-z]?[0-9]*', molecule):
        n = [int(s) for s in re.findall('\d+', e)]
        if len(n) == 0:
            n = 1
        else:
            n = n[0]
        symbol = re.findall('[A-Z][a-z]?', e)[0]
        m += elements[symbol] * n
    return m
#returns mass of SIMPLE molecules in grams/mole
def mass(molecule):
    m = 0
    #Hydrated compounds are split with '*'
    if '*' in molecule:
        a, b = molecule.split('*')
        hydration = re.findall('[0-9]*[A-Z]', b)[0][:-1]
        if len(hydration) == 0:
            hydration = 1
        else:
            hydration = int(hydration)
        return mass(a) + hydration * mass(b.replace(str(hydration), '', 1))
    
    #Deals with parentheses
    #Assumes only one layer
    groups = re.findall('\([^\(\)]+\)[0-9]*', molecule)
    for group in groups:
        n = re.findall('\)[0-9]*', group)
        n = n[0]
        n = n[1:]
        if len(n) == 0:
            n = 1
        else:
            n = int(n)
        m += n * massHelper(group)
        molecule = molecule.replace(group, '', 1)
    
    return m + massHelper(molecule)

tests = ['CH4', 'H2SO4', 'H2O', 'CO2', 'NH4OH', 'K4[Fe(CN)6]',
         '(NH4)2SO4', 'C60', 'Fe2(SO4)3', 'CH3(CH2)5CH3', 'CuSO4*5H2O']
#tests = ['NaBr', 'PbSO4', 'Ca(OH)2', 'Na3PO4', '(NH4)2CO3', 'C6H12O6',
#         'Fe3(PO4)2', '(NH4)2S', 'Zn(C2H3O2)2', 'AgF']

for t in tests:
    print(t, mass(t))


