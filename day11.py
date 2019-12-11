from virtual_machines import IntCodeMachine
import matplotlib.pyplot as plt


def run_robot(white_tiles=None):
    been_painted = set()
    white_tiles = {white_tiles}
    robot_pos, robot_dir = 0, 1j
    vm = IntCodeMachine(program='input.txt')
    while not vm.halted:
        current_colour = 1 if robot_pos in white_tiles else 0
        vm.input_buffer.append(current_colour)
        vm.run()
        assert len(vm.output_buffer) == 2
        robot_dir *= 1j if vm.output_buffer.pop() == 0 else -1j
        new_colour = vm.output_buffer.pop()
        if new_colour != current_colour and robot_pos not in been_painted:
            been_painted.add(robot_pos)
        if new_colour == 1:
            white_tiles.add(robot_pos)
        else:
            white_tiles.discard(robot_pos)
        robot_pos += robot_dir
    return been_painted, white_tiles


# part_1
painted, _ = run_robot()
# part_2
_, painted_white = run_robot(white_tiles=0)

print(f'Part 1: {len(painted)}')
plt.scatter(*zip(*[(p.real, p.imag) for p in painted_white]))
plt.show()
