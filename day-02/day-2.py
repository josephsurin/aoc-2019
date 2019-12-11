from intcode import execute
instructions = [int(x) for x in open('input').read().strip().split(',')]

fixed = instructions[::]
fixed[1] = 12
fixed[2] = 2

# part 1
print('part 1', execute(fixed)[0])

# part 2
# replace address 1 (noun) and address 2 (verb) with something in (0,99)
for noun in range(100):
    for verb in range(100):
        fixed = instructions[::]
        fixed[1] = noun
        fixed[2] = verb
        d = execute(fixed)
        if d != -1 and d[0] == 19690720:
            print('part 2', 100*noun+verb)
