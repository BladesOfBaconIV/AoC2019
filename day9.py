from virtual_machines import IntCodeMachine

vm = IntCodeMachine(program='input.txt')
vm.input_buffer.append(1)
vm.run()
assert len(vm.output_buffer) == 1
part_1 = vm.output_buffer.pop()

vm.respin()
vm.input_buffer.append(2)
vm.run()
assert len(vm.output_buffer) == 1
part_2 = vm.output_buffer.pop()

print(f'{part_1=}, {part_2=}')