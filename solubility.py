# generate random salts

cations = [("Cu", 1), ("Cu", 2), ("Fe", 2), ("Fe", 3), ("Mn", 2), ("Mn", 4)]
anions = []

alkali = ["Li", "Na", "K", "Rb", "Cs", "Fr"]
ammonium = ["NH4"]
rule4_except1 = ["Ag"]
rule4_except2 = ["Pb", "Hg2"]
rule4_except = rule4_except1 + rule4_except2
rule56_except = ["Ba", "Sr", "Ca"]
rule5_except = rule56_except + rule4_except + ["Hg"]
rule6_except = rule56_except + alkali
alkaline_earth = ["Be", "Mg", "Ca", "Sr", "Ba", "Ra"]
rule7_except = alkali + alkaline_earth
rule8_except = alkali + ammonium

rule3 = ["NO3", "ClO3", "ClO4", "C2H3O2"]
rule4 = ["Cl", "Br", "I"]
sulfate = ["SO4"]
hydroxide = ["OH"]
sulfide = ["S"]
rule8_2 = ["SO3", "CO3", "CrO4"]
rule8_3 = ["PO4"]
rule8 = rule8_2 + rule8_3

cations.extend(map(lambda x: (x, 1), alkali + ammonium + rule4_except1))
cations.extend(map(lambda x: (x, 2), rule4_except2 + rule5_except + alkaline_earth))

anions.extend(map(lambda x: (x, 1), rule3 + rule4 + hydroxide))
anions.extend(map(lambda x: (x, 2), sulfate + sulfide + rule8_2))
anions.extend(map(lambda x: (x, 3), rule8_3))

rules = [
    ("rule 1", lambda cat, an: "soluble" if cat in alkali else None),
    ("rule 2", lambda cat, an: "soluble" if cat in ammonium else None),
    ("rule 3", lambda cat, an: "soluble" if an in rule3 else None),
    ("rule 4", lambda cat, an: ("soluble" if cat not in rule4_except else "insoluble") if an in rule4 else None),
    ("rule 5", lambda cat, an: ("soluble" if cat not in rule5_except else "insoluble") if an in sulfate else None),
    ("rule 6", lambda cat, an: ("insoluble" if cat not in rule6_except else "soluble") if an in hydroxide else None),
    ("rule 7", lambda cat, an: ("insoluble" if cat not in rule7_except else "soluble") if an in sulfide else None),
    ("rule 8", lambda cat, an: ("insoluble" if cat not in rule8_except else "soluble") if an in rule8 else None),
]

def results(cat, an):
    return list(map(lambda a: a[1](cat[0], an[0]), rules))

def soluble(cat, an):
    for name, rule in rules:
        result = rule(cat[0], an[0])
        if result is not None:
            print(result, "by", name)

complex_signals = frozenset("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
def complex(ion):
    return sum(1 for c in ion if c in complex_signals) > 1

def name_part(ion, coef):
    if coef == 1: return ion
    if complex(ion):
        return "(%s)%d" % (ion, coef)
    else:
        return "%s%d" % (ion, coef)
def name(cat, an):
    from fractions import gcd
    g = gcd(cat[1], an[1])
    ccoef = an[1] // g
    acoef = cat[1] // g
    return name_part(cat[0], ccoef) + name_part(an[0], acoef)

while True:
    from random import choice
    try:
        cat = choice(cations)
        an = choice(anions)
        ans = input(name(cat, an) + "? ")
        if ans == "quit": break
        res = results(cat, an)
        if not all((r == ans or r is None) for r in res):
            soluble(cat, an)
    except KeyboardInterrupt:
        break
