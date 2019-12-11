d = [int(x) for x in open('input').readlines()]

# part 1
print('part 1', sum(x//3-2 for x in d))

# part 2
def calc_fuel_req(m):
    if m//3-2 < 0: return 0
    return m//3-2
s = 0
for c in d:
    m = calc_fuel_req(c)
    s += m
    while m != 0:
        m = calc_fuel_req(m)
        s += m
print('part 2', s)
