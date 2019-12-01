with open('input.txt', 'r') as f:
    x = [int(l) for l in f.readlines()]


def part_1(modules):
    return sum(max((m//3)-2, 0) for m in modules)


def part_2(modules):
    t_fuel = 0
    while any(modules):
        t_fuel += part_1(modules)
        modules = [max((m//3)-2, 0) for m in modules]
    return t_fuel


print(f'part 1 {part_1(x)}\npart 2 {part_2(x)}')
