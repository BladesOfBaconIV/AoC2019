from virtual_machines import IntCodeMachine
from itertools import permutations

with open('input.txt', 'r') as f:
    p = list(map(int, f.read().split(',')))


def series_amps(phase_range, no_feedback=True):
    max_output = 0
    for phase_combo in permutations(phase_range):
        amps = [IntCodeMachine(program=p) for _ in phase_range]
        for i in range(no_feedback, len(amps)):
            amps[i].input_buffer = amps[i - 1].output_buffer
            amps[i].input_buffer.append(phase_combo[i])
        if no_feedback:
            amps[0].input_buffer.append(phase_combo[0])
        amps[0].input_buffer.append(0)
        while not amps[-1].halted:
            for i, amp in enumerate(amps):
                amp.run()
        max_output = max(max_output, amps[-1].output_buffer[-1])
    return max_output


phases_part_1 = tuple(range(5))
phases_part_2 = tuple(range(5, 10))
print(f'{series_amps(phases_part_1, no_feedback=True)=}, {series_amps(phases_part_2, no_feedback=False)=}')