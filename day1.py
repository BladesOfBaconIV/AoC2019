with open('input.txt', 'r') as f:
    x = [int(l) for l in f.readlines()]


def fuel(module):
    return max((module // 3) - 2, 0)


def t_fuel(module):
    tot = 0
    while module := fuel(module):
        tot += module
    return tot


def part_1(modules):
    return sum(fuel(m) for m in modules)


def part_2(modules):
    return sum(t_fuel(m) for m in modules)


print(f'{part_1(x)=}\n{part_2(x)=}')
