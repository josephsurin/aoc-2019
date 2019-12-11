lower, upper = [int(x) for x in open('input').read().split('-')]

# part 1
def two_adj(x):
    m = [str(x)[i:i+2] for i in range(len(str(x)) - 1)]
    return any(len(set(c)) == 1 for c in m)

def non_dec(x):
    return str(x) == ''.join(sorted(str(x)))

def valid_pw(x):
    return two_adj(x) and non_dec(x) and len(str(x)) == 6

possible = []
for x in range(lower, upper):
    if valid_pw(x):
        possible.append(x)
print('part 1', len(possible)) # 2132

# part 2
def two_adj_2(x):
    m = [str(x)[i:i+2] for i in range(len(str(x)) - 1)]
    return any(len(set(c)) == 1 and m.count(c) == 1 for c in m)

def valid_pw_2(x):
    return two_adj_2(x) and non_dec(x) and len(str(x)) == 6
possible_2 = []
for x in range(lower, upper):
    if valid_pw_2(x):
        possible_2.append(x)
print('part 2', len(possible_2)) # 1411

