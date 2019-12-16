from gmpy2 import lcm, gcd
inp = open('input').read().strip()

# part 1
base = [0,1,0,-1]
def elongate(b, t):
    o = []
    for i in range(len(b)*t):
        o.append(b[i//t])
    return o
bases = [elongate(base, i+1) for i in range(700)]

def go_phase1(inp):
    inp = [int(x) for x in inp]
    o = ''
    for p in range(len(inp)):
        out = 0
        for i,x in enumerate(inp):
            # pattern = elongate(base, p+1)
            pattern = bases[p]
            out += x*pattern[(p-i-1)%len(pattern)]
        o += str(abs(out)%10)
    return o
for _ in range(100):
    inp = go_phase1(inp)
print('part 1', inp[:8])

# part 2
inp = open('input').read().strip()*10000
offset = int(inp[:7])
inp = inp[offset:]
def go_phase2(inp):
    inp = [int(x) for x in inp]
    o = ''
    s = 0
    for i in range(len(inp)-1, 0, -1):
        s += inp[i]
        o += str(s%10)
    return ''.join(reversed(o))

for _ in range(100):
    inp = go_phase2(inp)
print('part 2', inp[:8])
