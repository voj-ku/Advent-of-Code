with open('../Data/Day 4/input.txt') as f:
    s = [row.strip() for row in f.readlines()]

# P1

def rng_fully_contained(input):
     rngs = [int(x) for x in sum([x.split('-') for x in [s for s in input.split(',')]],[])]
     minv, maxv = min(rngs), max(rngs)
     return [minv,maxv] in (rngs[:2], rngs[2:])
sum([rng_fully_contained(l) for l in s])

# P2
def rng_partially_contained(input):
     rngs = [int(x) for x in sum([x.split('-') for x in [s for s in input.split(',')]],[])]
     return not ((rngs[2]>rngs[1]) | (rngs[0]>rngs[3]))
sum([rng_partially_contained(l) for l in s])
