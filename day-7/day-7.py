from itertools import permutations
from intcode2 import execute

I = [int(x) for x in open('input').read().split(',')]

def get_signal(I, ps):
    m = 0
    for i in range(len(ps)):
        I, [m] = execute(I, [ps[i], m])
    return m

print('part 1', max(get_signal(I, x) for x in permutations([0,1,2,3,4])))
