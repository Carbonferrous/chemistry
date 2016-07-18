class Counter(dict):
    def __init__(self):
        super().__init__()
    def __iadd__(self, o):
        for a in o:
            self[a] += o[a]
        return self
    def __missing__(self, _):
        return 0
    def __mul__(self, c):
        r = Counter()
        for a in self:
            r[a] = self[a] * c
        return r
    def __add__(self, o):
        r = Counter()
        r += self
        r += o
        return r

def parse_compound(x):
    print('parsing', x)
    import re
    ret = Counter()
    if x == '':
        return ret # next stmt raises if empty
    c, *h = x.split('*')
    for j in h:
        print('hydrate', j)
        m = re.match(r'\d*', j)
        ret += parse_compound(j[m.end():]) * int(m.group(0) or '1')
    b = 0
    l = 0
    s = ''
    for m in re.finditer(r'[]()[]', c):
        i = m.start()
        if m.group() in '([':
            if b == 0:
                s += c[l:i]
                l = i + 1
            b += 1
        else:
            b -= 1
            if b == 0:
                m = re.match(r'\d*', c[i+1:]) # may be dangerous for large c
                ret += parse_compound(c[l:i]) * int(m.group(0) or '1')
                l = m.end() + i + 1
    s += c[l:]
    if len(s) == 0:
        return ret
    print('after removal:', s)
    a = re.sub(r'([A-Z])', r'|\1', s).lstrip('|').split('|')
    for g in a:
        e, cc, *_ = re.sub(r'(?<!\d)(\d)', r'|\1', g).split('|') + ['1']
        c = int(cc)
        ret[e] += c
    return ret

tests = ['CH4', 'H2SO4', 'H2O', 'CO2', 'NH4OH', 'K4(Fe(CN)6)',
         '(NH4)2SO4', 'C60', 'Fe2(SO4)3', 'CH3(CH2)5CH3', 'CuSO4*5H2O',
         'NaBr', 'PbSO4', 'Ca(OH)2', 'Na3PO4', '(NH4)2CO3', 'C6H12O6',
         'Fe3(PO4)2', '(NH4)2S', 'Zn(C2H3O2)2', 'AgF', 'ClO4', 'SO4', 'CO3', 'NH4',
         'MnO3', 'C6CH3(NO2)2H2', 'Fe3[Co(NH3)6((SiO4))(O4)]2*5Ca(SO4)65']

for t in tests:
    print('Original', t)
    print(parse_compound(t))
