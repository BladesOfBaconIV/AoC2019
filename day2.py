with open('input.txt', 'r') as f:
    p = list(map(int, f.read().split(',')))


def run(program, noun, verb, end_add=0):
    i = 0
    program[1], program[2] = noun, verb
    while (command := program[i]) != 99:
        a, b = program[program[i + 1]], program[program[i + 2]]
        program[program[i + 3]] = a + b if command == 1 else a * b
        i += 4
    return program[end_add]


def part_2(program, desired_out):
    noun, verb = 0, 0
    ans1 = run(program[:], noun, verb)
    delta_noun = run(program[:], noun + 1, verb) - ans1
    delta_verb = run(program[:], noun, verb + 1) - ans1
    delta_desired = desired_out - ans1
    noun = delta_desired//delta_noun
    verb = (delta_desired-noun*delta_noun)//delta_verb
    return noun, verb


print(f'{run(p[:], 12, 2)=}, {part_2(p[:], 19690720)=}')
