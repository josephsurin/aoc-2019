def get_params(I, eip, num_args):
    param_types = str(I[eip])[:-2].rjust(num_args, '0')
    return [(I[eip + i + 1], p) for i, p in enumerate(reversed(param_types))]

def eval_param(I, param):
    v, p = param
    if p == '1': return v
    if p == '0': return I[v]

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

INITIALISED_C = 50
EXECUTING_C = 51
WAITING_FOR_INPUT_C = 52
EXECUTION_FINISHED_C = 0
ERROR_C = 1

class IntCode:
    def __init__(self, I):
        self.status = INITIALISED_C
        self.eip = 0
        self.inp_ctr = 0
        self.inps = []
        self.outputs = []
        self.I = I[::]

    def get_state(self):
        return { 'I': self.I,
                 'eip': self.eip,
                 'inp_ctr': self.inp_ctr,
                 'inps': self.inps,
                 'outputs': self.outputs,
                 'status': self.status
         }

    def inp(self, new_inps):
        self.inps += new_inps

    def run(self):
        self.status = EXECUTING_C

        op = self.I[self.eip] % 100
        while op != FIN_OP:
            if op == ADD_OP:
                a1, a2, a3 = get_params(self.I, self.eip, ADD_ARGS)
                self.I[a3[0]] = eval_param(self.I, a1) + eval_param(self.I, a2)
                self.eip += ADD_ARGS + 1

            elif op == MUL_OP:
                a1, a2, a3 = get_params(self.I, self.eip, MUL_ARGS)
                self.I[a3[0]] = eval_param(self.I, a1) * eval_param(self.I, a2)
                self.eip += MUL_ARGS + 1

            elif op == STR_OP:
                a1 = self.I[self.eip + 1]
                if self.inp_ctr >= len(self.inps):
                    self.status = WAITING_FOR_INPUT_C
                    return WAITING_FOR_INPUT_C
                else:
                    self.I[a1] = self.inps[self.inp_ctr]
                self.inp_ctr += 1
                self.eip += STR_ARGS + 1

            elif op == LOD_OP:
                a1 = get_params(self.I, self.eip, LOD_ARGS)[0]
                self.outputs.append(eval_param(self.I, a1))
                self.eip += LOD_ARGS + 1

            elif op == JIT_OP:
                a1, a2 = get_params(self.I, self.eip, JIT_ARGS)
                if eval_param(self.I, a1) != 0:
                    self.eip = eval_param(self.I, a2)
                else:
                    self.eip += JIT_ARGS + 1

            elif op == JIF_OP:
                a1, a2 = get_params(self.I, self.eip, JIT_ARGS)
                if eval_param(self.I, a1) == 0:
                    self.eip = eval_param(self.I, a2)
                else:
                    self.eip += JIT_ARGS + 1

            elif op == LST_OP:
                a1, a2, a3 = get_params(self.I, self.eip, LST_ARGS)
                if eval_param(self.I, a1) < eval_param(self.I, a2):
                    self.I[a3[0]] = 1
                else:
                    self.I[a3[0]] = 0
                self.eip += LST_ARGS + 1

            elif op == EQL_OP:
                a1, a2, a3 = get_params(self.I, self.eip, EQL_ARGS)
                if eval_param(self.I, a1) == eval_param(self.I, a2):
                    self.I[a3[0]] = 1
                else:
                    self.I[a3[0]] = 0
                self.eip += EQL_ARGS + 1

            else:    
                print('ERROR IN EXECUTION AT', self.eip)
                self.status = ERROR_C
                return ERROR_C
            
            op = self.I[self.eip] % 100
        self.status = EXECUTION_FINISHED_C
        return EXECUTION_FINISHED_C
