from intcode2 import IntCode
from random import randint

I = [int(x) for x in open('input').read().split(',')]
S = IntCode(I)

# part 1
S.run()
npos = [1j,-1j,-1,1]
def build_map():
    m = {}
    pos = 0+0j
    m[pos] = '.'
    c = 0
    while 1:
        d = randint(1,4)
        c += 1
        S.inp([d]) 
        S.run()
        s = S.get_state()['outputs'][-1]
        if s == 0:
            m[pos+npos[d-1]] = '#'
        if s == 1:
            pos += npos[d-1]
            m[pos] = '.'
        if s == 2:
            pos += npos[d-1]
            m[pos] = 'G'
        if 'G' in m.values() and c > 100000:
            break
        elif c > 100000:
            c = 0
    return m

def draw_grid(m):
    # find boundaries
    min_x = min([int(p.real) for p in m])
    max_x = max([int(p.real) for p in m])
    min_y = min([int(p.imag) for p in m])
    max_y = max([int(p.imag) for p in m])
    g = ''
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            if (x+y*1j) in m:
                g += m[x+y*1j]
            else:
                g += ' '
        g += '\n'
    return g

from pickle import loads, dumps
# m = build_map()
# open('mapdata.pickle', 'wb').write(dumps(m))
m = loads(open('mapdata.pickle', 'rb').read())
# print(draw_grid(m))

def get_neighbours(m, p):
    return [p+d for d in npos if p+d in m and m[p+d] != '#']
def dist_to_G(m):
    visited = []
    searchq = get_neighbours(m, (0+0j))
    distances = {n:1 for n in searchq}
    distances[(0+0j)] = 0
    while searchq:
        cn = searchq.pop(0)
        visited.append(cn)
        distances[cn] = 1 + min([distances[n] for n in get_neighbours(m, cn) if n in distances])
        if m[cn] == 'G':
            return distances[cn]
        searchq += [n for n in get_neighbours(m, cn) if n not in visited]
print('part 1', dist_to_G(m)) # 230

def get_dists(m, start):
    visited = []
    searchq = get_neighbours(m, start)
    distances = {n:1 for n in searchq}
    distances[start] = 0
    while searchq:
        cn = searchq.pop(0)
        visited.append(cn)
        distances[cn] = 1 + min([distances[n] for n in get_neighbours(m, cn) if n in distances])
        searchq += [n for n in get_neighbours(m, cn) if n not in visited]
    return distances

G = [p for p in m if m[p] == 'G'][0]
D = get_dists(m, G)
print('part 2', max(D.values())) # 288
