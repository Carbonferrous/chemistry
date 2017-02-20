import re


def bracechecker(molecule):
    pLevel = 0
    bLevel = 0
    for c in molecule:
        pLevel += (c == '(') - (c == ')')
        bLevel += (c == '[') - (c == ']')
        if pLevel < 0:
            raise Exception('parenthesis mismatch - too many )')
        if bLevel < 0:
            raise Exception('bracket mismatch - too many ]')
    if pLevel > 0:
        raise Exception('parenthesis mismatch - too many (')
    if bLevel > 0:
        raise Exception('bracket mismatch - too many [')
    return True


class ElementCount(dict):
    def __init__(self):
        super().__init__()

    def __iadd__(self, o):
        for a in o:
            self[a] += o[a]
        return self

    def __missing__(self, _):
        return 0

    def __mul__(self, c):
        r = ElementCount()
        for a in self:
            r[a] = self[a] * c
        return r

    def __add__(self, o):
        r = ElementCount()
        r += self
        r += o
        return r


class Molecule:
    def __init__(self, compoundName):
        self.name = compoundName
        self.count = self.__parse_molecule(compoundName)
        self.mass = self.__getmass()

    def __eq__(self, o):
        return self.name == o.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def __getmass(self):
        # open and read elements.txt
        elementdata = {}
        try:
            f = open('elements.txt')
        except FileNotFoundError:
            return 0
        for line in f:
            symbol, name, mass = line.strip().split(' ')
            mass = float(mass)
            elementdata[symbol] = mass
        # cycles through each element in the counter and calculates the mass
        m = 0
        for k in self.count:
            try:
                m += elementdata[k] * self.count[k]
            except KeyError:
                return 0
        return m

    def __parse_molecule(self, molecule):
        counter = ElementCount()
        assert bracechecker(molecule)
        assert molecule != ''
        # coefficient in front of molecule
        self.coeff = re.match('[0-9]*', molecule).group(0)
        # if no coefficient, set to 1, else rename molecule
        if self.coeff == '':
            self.coeff = 1
        else:
            self.coeff = int(self.coeff)
            molecule = re.split('[0-9]+', molecule, maxsplit=1)[1]
            self.name = molecule
        # remove charges ^
        molecule = re.sub(r'\^[+-]?\d*[+-]?', '', molecule)
        # hydrates
        molecule, *hy = molecule.split('*')
        for h in hy:
            m = re.match(r'\d*', h)
            counter += self.__parse_molecule(h[m.end():]) * int(m.group(0) or '1')
        # handles parenthesis
        l = 0
        i, j = 0, 0
        mol = ''
        for p in re.finditer(r'[]()[]', molecule):
            if p.group() in '([':
                if l == 0:
                    i = p.start()
                    mol += molecule[j: i]
                l += 1
            else:
                l -= 1
                if l == 0:
                    j = p.end()
                    m = re.match(r'\d*', molecule[j:])
                    counter += self.__parse_molecule(molecule[i+1:j-1]) * int(m.group(0) or '1')
                    j += m.end()
        mol += molecule[j:]
        molecule = mol
        # elements
        assert molecule == ''.join(re.findall(r'[A-Z][a-z]*\d*', molecule))
        for e in re.findall(r'[A-Z][a-z]*\d*', molecule):
            ele, m, *_ = re.sub(r'(?<!\d)(\d)', r'|\1', e).split('|') + ['1']
            counter[ele] += int(m)
        return counter


class Reaction:
    def __init__(self, reaction):
        self.reaction = reaction
        self.__parse_reaction()

    def __add__(self, o):
        pass

    def __mul__(self, o):
        pass

    def __str__(self):
        return self.reaction

    def __repr__(self):
        return self.__str__()

    def __parse_reaction(self):
        assert bracechecker(self.reaction)
        assert self.reaction != ''
        assert re.search(r'<?=>?', self.reaction) is not None
        # seperates the reaction into reactants and products
        r, p = re.split(r'\s*<?=>?\s*', self.reaction)
        self.reactants = list(map(Molecule, re.split(r'\s*\+\s*', r)))
        self.products = list(map(Molecule, re.split(r'\s*\+\s*', p)))
        assert len(self.reactants) > 0 and len(self.products) > 0
        # gets all of the elements involved in the reaction
        keyList = []
        for x in self.reactants+self.products:
            keyList += list(x.count.keys())
        keyList = list(set(keyList))
        keyList.sort()
        # gets coefficient of each reactant
        self.rcoeff = list(a.coeff for a in self.reactants)
        self.pcoeff = list(a.coeff for a in self.products)
        # computes the homogenous system of linear equations to be solved
#        self.A = [[i.count[k] for i in self.reactants]+[-j.count[k] for j in self.products] for k in keyList]
        # solves the system for the coefficents of molecules in reaction
#        print(self.reactants, self.products, keyList)
#        print(A)
#        coeff = [i for i in range(len(self.reactants) + len(self.products))]
        # splits coefficients into reactants and products
#        assert len(coeff) == len(self.reactants) + len(self.products)
#        self.rcoeff = coeff[:len(self.reactants)]
#        self.pcoeff = coeff[len(self.reactants):]

molecules = ['CH4', 'H2SO4', 'H2O', 'CO2', 'NH4OH', 'K4[Fe(CN)6]',
             '(NH4)2SO4', 'C60', 'Fe2(SO4)3', 'CH3(CH2)5CH3', 'CuSO4*5H2O',
             'NaBr', 'PbSO4', 'Ca(OH)2', 'Na3PO4', '(NH4)2CO3', 'C6H12O6',
             'NH4ClO4', 'Fe3(PO4)2', '(NH4)2S', 'Zn(C2H3O2)2', 'AgF', 'ClO4^-',
             'SO4^2-', 'CO3^-2', 'NH4^+', 'MnO3', 'C6CH3(NO2)2H2',
             'Fe3[Co(NH3)6((SiO4))(Dmg)]2^3+*5Ca(SO4)65']

for t in molecules:
    a = Molecule(t)
    print(a.name, a.count, a.mass)

equations = ['2Fe + 3Cl2 = 2FeCl3',
             '2SO4 = 2SO3 + O2',
             'KMnO4 + HCl = KCl + MnCl2 + H2O + Cl2',
             'K4Fe(CN)6 + H2SO4 + H2O = K2SO4 + FeSO4 + (NH4)2SO4 + CO',
             '2C6H5COOH + 15O2 = 14CO2 + 6H2O',
             'K4Fe(CN)6 + KMnO4 + H2SO4 = KHSO4 + Fe2(SO4)3 + MnSO4 + HNO3 + CO2 + H2O',
             'PhCH3 + KMnO4 + H2SO4 = PhCOOH + K2SO4 + MnSO4 + H2O',
             'CuSO4*5H2O = CuSO4 + H2O']

for e in equations:
    print(e)
    a = Reaction(e)
    print(a.reaction)
#    print(a.A)
#    print('Equations:', len(a.A), 'Unknowns:', len(a.A[0]))
    print(a.rcoeff, a.pcoeff)
    print(a.reactants, a.products)
    print()
