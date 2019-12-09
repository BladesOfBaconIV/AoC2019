from collections import defaultdict
from operator import add, mul, lt, eq


def get_param_modes(opcode):
    opcode //= 10
    return ((opcode := opcode // 10) % 10 for _ in range(3))


def debug_wrapper(func):
    def wrapper(obj, *args, **kwargs):
        info = func(obj, *args, **kwargs)
        if obj.debug:
            print(f'{func.__name__}: {info}')
    return wrapper


def load_program(program):
    memory = defaultdict(int)
    if type(program) is str:
        with open(program, 'r') as f:
            program = list(map(int, f.read().split(',')))
    for address, value in enumerate(program):
        memory[address] = value
    return memory


class IntCodeMachine:

    def __init__(self, program, *, halt_code=99, debug=False):
        self.ip = 0
        self.memory = load_program(program)
        self.program = program
        self.input_buffer = []
        self.output_buffer = []
        self.halt_code = halt_code
        self.paused = False
        self.halted = False
        self.rel_ip = 0

        self.lookup_table = {
            1: (self.math2, {'func': add}),
            2: (self.math2, {'func': mul}),
            3: (self.input, {'write': False}),
            4: (self.input, {'write': True}),
            5: (self.jump, {'jmp_if_false': False}),
            6: (self.jump, {'jmp_if_false': True}),
            7: (self.math2, {'func': lt}),
            8: (self.math2, {'func': eq}),
            9: (self.rel_ip_change, {}),
        }

        self.debug = debug

    def respin(self, new_program=None):
        self.output_buffer = []
        self.input_buffer = []
        self.program = self.program if not new_program else new_program
        self.memory = load_program(self.program)
        self.ip = 0
        self.rel_ip = 0

    def run(self, *, offset=0):
        self.ip += offset
        self.paused = False
        while (opcode := self.read(mode=1)) % 100 != self.halt_code and not self.paused:
            func, args = self.lookup_table[opcode % 100]
            func(opcode, **args)
        self.halted = opcode % 100 == self.halt_code

    def read(self, mode=0, offset=0):
        if mode == 0:
            return self.memory[self.memory[self.ip + offset]]
        elif mode == 1:
            return self.memory[self.ip + offset]
        elif mode == 2:
            return self.memory[self.rel_ip + self.memory[self.ip + offset]]

    def write(self, value, mode=0, offset=0):
        if mode == 0:
            self.memory[self.memory[self.ip + offset]] = value
        elif mode ==2:
            self.memory[self.rel_ip + self.memory[self.ip + offset]] = value

    def read_block(self, length, modes):
        return (self.read(mode=m, offset=1+n) for m, n in zip(modes, range(length)))

    @debug_wrapper
    def math2(self, opcode, func):
        a_mode, b_mode, c_mode = get_param_modes(opcode)
        a, b = self.read_block(2, (a_mode, b_mode))
        self.write(func(a, b), mode=c_mode, offset=3)
        self.ip += 4
        return f'{opcode=}, {func=}, {a=}, {a_mode=}, {b=}, {b_mode=}, {c_mode=}'

    @debug_wrapper
    def input(self, opcode, write):
        mode, *_ = get_param_modes(opcode)
        if write:
            self.output_buffer.append(self.read(mode=mode, offset=1))
        else:
            if not self.input_buffer:
                self.paused = True
                return f'{opcode=}, {mode=}, paused'
            self.write(self.input_buffer.pop(0), mode=mode, offset=1)
        self.ip += 2
        return f'{opcode=}, {mode=}'

    @debug_wrapper
    def jump(self, opcode, jmp_if_false):
        a_mode, b_mode, _ = get_param_modes(opcode)
        val, jmp_to = self.read_block(2, (a_mode, b_mode))
        if jmp_if_false and not val:
            self.ip = jmp_to
        elif not jmp_if_false and val:
            self.ip = jmp_to
        else:
            self.ip += 3
        return f'{opcode=}, {jmp_if_false=}, {val=}, {jmp_to=}'

    @debug_wrapper
    def rel_ip_change(self, opcode):
        a_mode, *_ = get_param_modes(opcode)
        rel_change = self.read(mode=a_mode, offset=1)
        self.rel_ip += rel_change
        self.ip += 2
        return f'{opcode=}, {rel_change=}, {self.rel_ip=}'
