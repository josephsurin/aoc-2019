from itertools import combinations

p1=[1, 4, 4]
p2=[-4, -1, 19]
p3=[-15, -14, 12]
p4=[-17, 1, 10]

ps = [[p1[::], [0,0,0]],[p2[::], [0,0,0]],[p3[::], [0,0,0]],[p4[::], [0,0,0]]]

def apply_grav(o1, o2):
    p1, v1 = o1
    p2, v2 = o2
    d = [0,0,0]
    if p1[0] > p2[0]:
        d[0] = -1
    elif p1[0] < p2[0]:
        d[0] = 1
    if p1[1] > p2[1]:
        d[1] = -1
    elif p1[1] < p2[1]:
        d[1] = 1
    if p1[2] > p2[2]:
        d[2] = -1
    elif p1[2] < p2[2]:
        d[2] = 1
    v1[0] += d[0]
    v1[1] += d[1]
    v1[2] += d[2]
    v2[0] -= d[0]
    v2[1] -= d[1]
    v2[2] -= d[2]

def apply_vel(o):
    p, v = o
    p[0] += v[0]
    p[1] += v[1]
    p[2] += v[2]

def go_step(ps):
    for o1, o2 in combinations(ps, 2):
        apply_grav(o1, o2)
    for o in ps:
        apply_vel(o)

def go_steps(ps, n):
    for _ in range(n):
        go_step(ps)

def energy(o):
    p, v = o
    pot = abs(p[0]) + abs(p[1]) + abs(p[2])
    kin = abs(v[0]) + abs(v[1]) + abs(v[2])
    return pot * kin

# part 1
go_steps(ps, 1000)
print('part 1', sum([energy(o) for o in ps]))

# part 2
from gmpy2 import lcm
'''
find the periods of the x y z positions and velocities; the cycle length is the lcm of these three values
'''

ps = [[p1[::], [0,0,0]],[p2[::], [0,0,0]],[p3[::], [0,0,0]],[p4[::], [0,0,0]]]
def get_axis_state(ps, axis):
    return [(o[0][::][axis], o[1][::][axis]) for o in ps]

def get_least_steps_to_repeat(ps):
    xc, yc, zc = 0, 0, 0
    x0 = get_axis_state(ps, 0)
    y0 = get_axis_state(ps, 1)
    z0 = get_axis_state(ps, 2)
    for i in range(100000000):
        go_step(ps)

        xs = get_axis_state(ps, 0)
        if xc == 0 and xs == x0:
            xc = i

        ys = get_axis_state(ps, 1)
        if yc == 0 and ys == y0:
            yc = i

        zs = get_axis_state(ps, 2)
        if zc == 0 and zs == z0:
            zc = i

        if xc > 0 and yc > 0 and zc > 0:
            break

    return lcm(lcm(xc+1, yc+1), zc+1)

print('part 2', get_least_steps_to_repeat(ps))
