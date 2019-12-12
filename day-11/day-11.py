from intcode2 import IntCode

I = [int(x) for x in open('input').read().split(',')]

# part 1
TURN_LEFT = 0
TURN_RIGHT = 1
pos = 0 + 0j
direction = 1j
visited = {pos: 0}
S = IntCode(I)
while S.get_state()['status'] != 0:
    if pos in visited:
        S.inp([visited[pos]])
    else:
        S.inp([0])
    S.run()
    col, dr = S.get_state()['outputs'][-2:]
    visited[pos] = col
    if dr == TURN_LEFT:
        direction *= 1j
    if dr == TURN_RIGHT:
        direction /= 1j
    pos += direction
print('part 1', len(visited))

# part 2
from PIL import Image
img = Image.new('1', (100,100))
def c_to_cart(z):
    return (int(z.real)+50, 50+int(z.imag))
TURN_LEFT = 0
TURN_RIGHT = 1
pos = 0 + 0j
direction = 1j
visited = {pos: 1}
S = IntCode(I)
while S.get_state()['status'] != 0:
    if pos in visited:
        S.inp([visited[pos]])
    else:
        S.inp([0])
    S.run()
    col, dr = S.get_state()['outputs'][-2:]
    visited[pos] = col
    img.putpixel(c_to_cart(pos), col)
    if dr == TURN_LEFT:
        direction *= 1j
    if dr == TURN_RIGHT:
        direction /= 1j
    pos += direction
img.save('part2.png')
print('part 2', 'part2.png')
