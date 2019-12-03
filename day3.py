from itertools import accumulate

DIR_TO_COMPLEX = {
    'U': 0+1j,
    'D': 0-1j,
    'L': -1,
    'R': +1,
}


def translate(path: iter) -> tuple:  # tuple of (direction, num_steps) tuples
    return tuple((DIR_TO_COMPLEX[instr[0]], int(instr[1:])) for instr in path)


with open('input.txt', 'r') as f:
    path_a, path_b = (translate(path.split(',')) for path in f.readlines())

steps_a = tuple(accumulate(d * 1 for d, steps in path_a for _ in range(steps)))
steps_b = tuple(accumulate(d * 1 for d, steps in path_b for _ in range(steps)))
intersections = set(steps_a) & set(steps_b)

part_1 = min(map(lambda i: abs(i.real) + abs(i.imag), intersections))
part_2 = min(map(lambda i: steps_a.index(i) + steps_b.index(i) + 2, intersections))

print(f'{part_1=}\n{part_2=}')
