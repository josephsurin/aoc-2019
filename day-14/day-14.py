inp = open('input').read().splitlines()
from collections import defaultdict
from math import ceil

# part 1
a_madeby_b = {}
for l in inp:
    i, out = l.split(' => ')
    inps = i.split(', ')
    I = []
    for ix in inps:
        v, t = ix.split(' ')
        I.append((int(v), t))
    v,t = out.split(' ')
    a_madeby_b[(int(v), t)] = I

def get_cost(y):
    leftovers = defaultdict(int)
    def _get_cost(x):
        xv, xt = x
        if xt == 'ORE':
            return xv
        targ = [targ for targ in a_madeby_b.keys() if targ[1] == xt][0]
        xv -= leftovers[xt] # take from inventory
        n = ceil(xv / targ[0]) # new needed
        leftovers[xt] = n * targ[0] - xv
        needed = a_madeby_b[targ]
        needed = [(v*n,t) for v,t in needed]
        return sum([_get_cost(s) for s in needed])
    return _get_cost(y)

print('part 1', get_cost((1, 'FUEL'))) # 843220

# part 2
ore_limit = 1000000000000
lo = 1
hi = 10000000
while lo < hi:
    mid = (lo + hi)//2
    x = get_cost((mid, 'FUEL'))
    if x > ore_limit:
        hi = mid - 1
    elif x < ore_limit:
        lo = mid
    else:
        break

print('part 2', mid - 1) # 2169535
