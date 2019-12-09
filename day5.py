from virtual_machines import IntCodeMachine

vm = IntCodeMachine(program='input.txt')
vm.input_buffer.append(1)
vm.run()
part_1_output = set(vm.output_buffer)

vm.respin()
vm.input_buffer.append(5)
vm.run()
assert len(vm.output_buffer) == 1

print(f'{part_1_output=}, {vm.output_buffer=}')