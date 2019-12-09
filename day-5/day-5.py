from intcode2 import execute

inp = [int(x) for x in open('input').read().split(',')]

execute(inp)
