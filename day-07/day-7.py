from itertools import permutations
from intcode2_ampmod import execute

I = [int(x) for x in open('input').read().split(',')]

def get_signal(I, ps):
    m = 0
    for i in range(len(ps)):
        _, [m] = execute(I, [ps[i], m])
    return m

# part 1
print('part 1', max(get_signal(I, x) for x in permutations([0,1,2,3,4]))) # 13848

# part 2
from intcode2_ampmod2 import IntCode
I = [int(x) for x in open('input').read().split(',')]

def get_signal(S, ps):
    i = 0 # current amplifier running
    m = 0 # signal to send to current amplifier
    hc = -1
    while S[4].get_state()['status'] != 0:
        s = S[i%5]
        ii = [ps[i], m] if i <= 4 else [m]
        s.inp(ii)
        hc = s.run()
        m = s.get_state()['outputs'][-1]
        i += 1
    return m

print('part 2', max(get_signal([IntCode(I) for _ in range(5)], x) for x in permutations([5,6,7,8,9]))) # 12932154
