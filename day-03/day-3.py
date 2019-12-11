inp = open('input').read().splitlines()
w1, w2 = [s.split(',') for s in inp]

# part 1
def get_segment_points(pos, mvmt):
    dv = { 'L': -1, 'U': 1j, 'R': 1, 'D': -1j }[mvmt[0]]
    dm = int(mvmt[1:]) + 1
    return [pos + dv*i for i in range(dm)]

def find_intersections(w1, w2):
    #finds the coordinate intersections of the two given wires relative to the central port
    intersections = set() 
    #build points for first wire to check against
    w1_pts = []
    w1_pos = 0 + 0j
    for d in w1:
        w1_pts.append(get_segment_points(w1_pos, d))
        w1_pos = w1_pts[-1][-1]
    w2_pos = 0 + 0j
    for d in w2:
        '''
        for each movement in the 2nd wire, need to check if intersects with any line segments from first wire
        keep track of the coordinate position of the 2nd wire
        '''
        w2_pts = get_segment_points(w2_pos, d)
        w2_pos = w2_pts[-1]
        w1_pos = 0 + 0j
        for c in w1_pts:
            intersections = intersections.union(set(c).intersection(w2_pts))
    return intersections - {0j}

def manhattan_distance(c):
    return abs(c.real) + abs(c.imag)

intersections = find_intersections(w1, w2)
print('part 1', min(manhattan_distance(x) for x in intersections)) # takes a while cause bad code... 352

# part 2
def count_steps(w_pts, pt):
    # returns num of steps required to get to pt from central port along the segments given by the w_pts 2d list
    s = 0
    for w in w_pts:
        if pt in w:
            s += w.index(pt)
            return s
        else:
            s += len(w) - 1
    return s
w1_pts = []
w1_pos = 0 + 0j
for d in w1:
    w1_pts.append(get_segment_points(w1_pos, d))
    w1_pos = w1_pts[-1][-1]
w2_pts = []
w2_pos = 0 + 0j
for d in w2:
    w2_pts.append(get_segment_points(w2_pos, d))
    w2_pos = w2_pts[-1][-1]
print('part 2', min(count_steps(w1_pts, x) + count_steps(w2_pts, x) for x in intersections)) # 43848
