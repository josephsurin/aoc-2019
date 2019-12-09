# slightly modified from prev questions to allow for more programmability; inputs are taken as a list in the 2nd argument and outputs are returned as a list in the 2nd element of the return value list
'''intcode machine interpreter
takes a list of integers and returns the final state (as a list of integers) from the execution of the given input'''

ADD_OP = 1
ADD_ARGS = 3

MUL_OP = 2
MUL_ARGS = 3

STR_OP = 3
STR_ARGS = 1

LOD_OP = 4
LOD_ARGS = 1

JIT_OP = 5
JIT_ARGS = 2

JIF_OP = 6
JIF_ARGS = 2

LST_OP = 7
LST_ARGS = 3

EQL_OP = 8
EQL_ARGS = 3

FIN_OP = 99

def get_params(I, eip, num_args):
    param_types = str(I[eip])[:-2].rjust(num_args, '0')
    return [(I[eip + i + 1], p) for i, p in enumerate(reversed(param_types))]

def eval_param(I, param):
    v, p = param
    if p == '1': return v
    if p == '0': return I[v]

def execute(I, inps):
    outputs = []
    inp_ctr = 0
    eip = 0
    op = I[eip] % 100
    while op != FIN_OP:
        if op == ADD_OP:
            a1, a2, a3 = get_params(I, eip, ADD_ARGS)
            I[a3[0]] = eval_param(I, a1) + eval_param(I, a2)
            eip += ADD_ARGS + 1

        elif op == MUL_OP:
            a1, a2, a3 = get_params(I, eip, MUL_ARGS)
            I[a3[0]] = eval_param(I, a1) * eval_param(I, a2)
            eip += MUL_ARGS + 1

        elif op == STR_OP:
            a1 = I[eip + 1]
            I[a1] = inps[inp_ctr]
            inp_ctr += 1
            eip += STR_ARGS + 1

        elif op == LOD_OP:
            a1 = get_params(I, eip, LOD_ARGS)[0]
            outputs.append(eval_param(I, a1))
            eip += LOD_ARGS + 1

        elif op == JIT_OP:
            a1, a2 = get_params(I, eip, JIT_ARGS)
            if eval_param(I, a1) != 0:
                eip = eval_param(I, a2)
            else:
                eip += JIT_ARGS + 1

        elif op == JIF_OP:
            a1, a2 = get_params(I, eip, JIT_ARGS)
            if eval_param(I, a1) == 0:
                eip = eval_param(I, a2)
            else:
                eip += JIT_ARGS + 1

        elif op == LST_OP:
            a1, a2, a3 = get_params(I, eip, LST_ARGS)
            if eval_param(I, a1) < eval_param(I, a2):
                I[a3[0]] = 1
            else:
                I[a3[0]] = 0
            eip += LST_ARGS + 1

        elif op == EQL_OP:
            a1, a2, a3 = get_params(I, eip, EQL_ARGS)
            if eval_param(I, a1) == eval_param(I, a2):
                I[a3[0]] = 1
            else:
                I[a3[0]] = 0
            eip += EQL_ARGS + 1

        else:    
            print('ERROR IN EXECUTION AT', eip)
            return -1
        op = I[eip] % 100
    return [I, outputs]
