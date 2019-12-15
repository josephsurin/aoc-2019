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

URB_OP = 9
URB_ARGS = 1

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
        self.rbo = 0
        self.inp_ctr = 0
        self.inps = []
        self.outputs = []
        self.I = I[::] + [0] * len(I) * 8

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

    def get_params(self, num_args):
        param_types = str(self.I[self.eip])[:-2].rjust(num_args, '0')
        return [(self.I[self.eip + i + 1], p) for i, p in enumerate(reversed(param_types))]

    def eval_param(self, param):
        v, p = param
        if p == '2': return self.I[self.rbo + v]
        if p == '1': return v
        if p == '0': return self.I[v]

    def eval_write_param(self, param):
        v, p = param
        if p == '2': return self.rbo + v
        if p == '0': return v

    def run(self):
        self.status = EXECUTING_C

        op = self.I[self.eip] % 100
        while op != FIN_OP:
            if op == ADD_OP:
                a1, a2, a3 = self.get_params(ADD_ARGS)
                self.I[self.eval_write_param(a3)] = self.eval_param(a1) + self.eval_param(a2)
                self.eip += ADD_ARGS + 1

            elif op == MUL_OP:
                a1, a2, a3 = self.get_params(MUL_ARGS)
                self.I[self.eval_write_param(a3)] = self.eval_param(a1) * self.eval_param(a2)
                self.eip += MUL_ARGS + 1

            elif op == STR_OP:
                a1 = self.get_params(STR_ARGS)[0]
                if self.inp_ctr >= len(self.inps):
                    self.status = WAITING_FOR_INPUT_C
                    return WAITING_FOR_INPUT_C
                else:
                    self.I[self.eval_write_param(a1)] = self.inps[self.inp_ctr]
                self.inp_ctr += 1
                self.eip += STR_ARGS + 1

            elif op == LOD_OP:
                a1 = self.get_params(LOD_ARGS)[0]
                self.outputs.append(self.eval_param(a1))
                self.eip += LOD_ARGS + 1

            elif op == JIT_OP:
                a1, a2 = self.get_params(JIT_ARGS)
                if self.eval_param(a1) != 0:
                    self.eip = self.eval_param(a2)
                else:
                    self.eip += JIT_ARGS + 1

            elif op == JIF_OP:
                a1, a2 = self.get_params(JIT_ARGS)
                if self.eval_param(a1) == 0:
                    self.eip = self.eval_param(a2)
                else:
                    self.eip += JIT_ARGS + 1

            elif op == LST_OP:
                a1, a2, a3 = self.get_params(LST_ARGS)
                if self.eval_param(a1) < self.eval_param(a2):
                    self.I[self.eval_write_param(a3)] = 1
                else:
                    self.I[self.eval_write_param(a3)] = 0
                self.eip += LST_ARGS + 1

            elif op == EQL_OP:
                a1, a2, a3 = self.get_params(EQL_ARGS)
                if self.eval_param(a1) == self.eval_param(a2):
                    self.I[self.eval_write_param(a3)] = 1
                else:
                    self.I[self.eval_write_param(a3)] = 0
                self.eip += EQL_ARGS + 1

            elif op == URB_OP:
                a1 = self.get_params(URB_ARGS)[0]
                self.rbo += self.eval_param(a1)
                self.eip += URB_ARGS + 1

            else:    
                print('ERROR IN EXECUTION AT', self.eip)
                self.status = ERROR_C
                return ERROR_C
            
            op = self.I[self.eip] % 100
        self.status = EXECUTION_FINISHED_C
        return EXECUTION_FINISHED_C
