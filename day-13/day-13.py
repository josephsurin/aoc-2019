from intcode2 import IntCode

I = [int(x) for x in open('input').read().split(',')]
S = IntCode(I)

# part 1
S.run()
o = S.get_state()['outputs']

def make_map(o):
    tiles = {} 
    p = [o[i:i+3] for i in range(0, len(o), 3)]
    for x,y,t in p:
        tiles[x - y*1j] = t
    return tiles
def count_blocks(m):
    return list(m.values()).count(2)
print('part 1', count_blocks(make_map(o)))

# part 2
def coords(x):
    return (x.real, x.imag)
I = [int(x) for x in open('input').read().split(',')]
I[0] = 2
S = IntCode(I)
S.run()
o = S.get_state()['outputs']
m = make_map(o)
def get_paddle_pos(m):
    return [x for x, t in m.items() if t == 3][0]
def get_ball_pos(m):
    return [x for x, t in m.items() if t == 4][0]
while count_blocks(m) > 0:
    px, py = coords(get_paddle_pos(m))
    bx, by = coords(get_ball_pos(m))
    if bx > px:
        S.inp([1])
    elif bx < px:
        S.inp([-1])
    else:
        S.inp([0])
    S.run()
    o = S.get_state()['outputs']
    m = make_map(o)
print('part 2', m[-1+0j]) # 16539
