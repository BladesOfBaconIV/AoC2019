from virtual_machines import IntCodeMachine

with open('input.txt', 'r') as f:
    p = list(map(int, f.read().split(',')))

vm_part1 = IntCodeMachine(p)
vm_part1.input_buffer.append(1)
vm_part1.run()

vm_part2 = IntCodeMachine(p)
vm_part2.input_buffer.append(5)
vm_part2.run()

print(f'{set(vm_part1.output_buffer)=}, {vm_part2.output_buffer=}')