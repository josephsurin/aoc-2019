'''intcode machine interpreter
takes a list of integers and returns the final state (as a list of integers) from the execution of the given input'''

ADD_OP = 1
ADD_ARGS = 3
MUL_OP = 2
MUL_ARGS = 3
FIN_OP = 99

def execute(I):
    eip = 0
    op = I[eip]
    while op != FIN_OP:
        if op == ADD_OP:
            a1, a2, a3 = I[eip+1], I[eip+2], I[eip+3]
            I[a3]  = I[a1] + I[a2]
            eip += ADD_ARGS + 1
        elif op == MUL_OP:
            a1, a2, a3 = I[eip+1], I[eip+2], I[eip+3]
            I[a3]  = I[a1] * I[a2]
            eip += MUL_ARGS + 1
        else:    
            print('ERROR IN EXECUTION AT', eip)
            return -1
        op = I[eip]
    return I
