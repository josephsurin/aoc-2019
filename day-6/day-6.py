inp = open('input').read().splitlines()

# part 1
'''
generate a graph between orbiting objects and for each object in the data set, count how many edges required to get to COM
'''
graph = [] # list of pairs (A, B) => A orbits B
objects = set()
for s in inp:
    B, A = s.split(')') # A orbits B
    graph.append((A, B))
    objects = objects.union({A,B})

def count_indirect(graph, A):
    c = 0
    while A != 'COM':
        A = [x for x in graph if x[0] == A][0][1]
        c += 1
    return c

print('part 1', sum(count_indirect(graph, o) for o in objects)) #takes forever because bad code as usual 139597

# part 2
'''
bfs from the object YOU orbits with target of the object SAN orbits
'''
def get_neighbours(graph, A):
    return [x[1] for x in graph if x[0] == A] + [x[0] for x in graph if x[1] == A]
start_point = [x for x in graph if x[0] == 'YOU'][0][1]
search_q = [start_point]
distances = { A: -1 for A in objects }
distances[start_point] = 0
visited = []
while search_q:
    S = search_q.pop(0)
    visited.append(S)
    if S == 'SAN':
        print('part 2', distances[S] - 1) # 286
        break
    for x in [x for x in get_neighbours(graph, S) if x not in visited]:
        search_q.append(x)
        distances[x] = distances[S] + 1
