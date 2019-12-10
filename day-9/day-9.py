from intcode2 import IntCode

I = [int(x) for x in open('input').read().split(',')]

# part 1
S = IntCode(I)
S.inp([1])
S.run()
print('part 1', S.get_state()['outputs'][0]) # 3598076521

# part 2
S = IntCode(I)
S.inp([2])
S.run()
print('part 2', S.get_state()['outputs'][0]) # 3598076521
