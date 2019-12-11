'''
functions:
    parse_map(map_ascii) => parses map ascii into a list of coordinates representing where asteroids are
    visible_count(astds, asteroid) => counts how many asteroids are visible in the map from the given asteroid
    is_in_los(astds, asteroid1, asteroid2) => True if asteroid1 and asteroid2 are in line of sight of each other
    get_line_points(asteroid1, asteroid2) => returns a list containing all of the points (coordintes) that lie between the straight line from asteroid1 to asteroid2

    all points are complex numbers, c, with c.real being horizontal displacement from (0,0) and c.imag being vertical displacement from (0,0) where -1j is the point immediately below (0,0) (i.e. (0,-1))
'''

# part 1
EPS = 0.00000000001

def parse_map(ma):
    asteroids = []
    ma = ma.splitlines()
    for y in range(len(ma)):
        for x in range(len(ma[0])):
            if ma[y][x] == '#':
                asteroids.append(x - y*1j) 
    return asteroids

def coords(complex_num):
    return (complex_num.real, complex_num.imag)

def get_line_points(p1, p2):
    if p1 == p2:
        return []
    x1, y1 = coords(p1)
    x2, y2 = coords(p2)
    if x1 == x2:
        m = 1 if y2 > y1 else -1
        return [(x1)+(y1+m*i)*1j for i in range(1, int(abs(y2 - y1)))]
    if y1 == y2:
        m = 1 if x2 > x1 else -1
        return [(x1+m*i)+(y1)*1j for i in range(1, int(abs(x2 - x1)))]
    pts = []
    m = (y2 - y1)/(x2 - x1)
    c = y1 - m*x1
    for x in range(int(min(x1, x2)), int(max(x1, x2))):
        for y in range(int(min(y1, y2)), int(max(y1, y2))):
            if abs(y - (m*x + c)) < EPS:
                pts.append(x + y*1j)
    return pts

def is_in_los(astds, a1, a2):
    if a1 == a2:
        return False
    line = get_line_points(a1, a2)
    return not any([a in line for a in astds if a != a1 and a != a2])

def visible_count(astds, a):
    return len([x for x in astds if is_in_los(astds, a, x)])

astds = parse_map(open('input').read())
print('part 1', max(visible_count(astds, a) for a in astds)) # 253

# part 2
'''
give each asteroid an angle (relative to the base) and then sort by the angle, then iterate through each and if that asteroid is in line of sight, remove it from the list and increment counter then proceed
'''
from math import atan, pi

def get_angle(pt):
    # returns clockwise angle relative to 0+0j from the positive vertical axis
    x, y = coords(pt)
    x_a, y_a = abs(x), abs(y)
    if x == 0:
        return 0 if y >= 0 else pi
    if y == 0:
        return pi/2 if x >=0 else 3*pi/2
    if x > 0 and y > 0:
        return atan(x_a/y_a)
    if x > 0 and y < 0:
        return pi/2 + atan(y_a/x_a)
    if x < 0 and y < 0:
        return pi + atan(x_a/y_a)
    if x < 0 and y > 0:
        return 3*pi/2 + atan(y_a/x_a)

def get_angles(astds, base):
    return [(a, get_angle(a - base)) for a in astds if a != base]

base = 11-19j

angs = sorted(get_angles(astds, base), key=lambda a: a[1])
ctr = 1
i = 0
Ang = -1
while ctr < 200:
    a, ang = angs[i%len(angs)]
    if abs(Ang - ang) < EPS:
        i += 1
        continue
    if is_in_los(astds, a, base):
        angs.remove((a, ang))
        astds.remove(a)
        Ang = ang
        ctr += 1
        i -= 1
    i += 1

t = next(angs[j%len(angs)][0] for j in range(i, i+100) if is_in_los(astds, angs[j%len(angs)][0], base))
x,y = coords(t)
print('part 2', int(x*100 - y)) # 815
