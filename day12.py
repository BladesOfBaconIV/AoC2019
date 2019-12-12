import numpy as np
import re

with open('input.txt', 'r') as f:
    moons = np.array([list(map(int, re.findall(r"-?\d+", line))) for line in f])


def update_pos(pos, vel):
    for moon in pos:
        vel += np.sign(moon - pos)
    pos += vel


# Part 1
steps = 1000
velocity = np.zeros(moons.shape, dtype=np.int32)
pos_part_1 = moons.copy()
for _ in range(steps):
    update_pos(pos_part_1, velocity)
energy = np.sum(np.multiply(np.sum(np.abs(pos_part_1), axis=1), np.sum(np.abs(velocity), axis=1)))

# Part 2
pos_part_2 = moons.copy()
velocity = np.zeros(moons.shape, dtype=np.int32)
update_pos(pos_part_2, velocity)
steps = 1
dimension_periods = [0, 0, 0]
while not all(dimension_periods):
    for i, v in enumerate(velocity.T):
        if not v.any() and not dimension_periods[i]:
            dimension_periods[i] = 2 * steps
    update_pos(pos_part_2, velocity)
    steps += 1
period_of_cycle = np.lcm.reduce(np.array(dimension_periods, dtype=np.int64))

print(f'Part 1: {energy=}, Part 2: {period_of_cycle=}')
