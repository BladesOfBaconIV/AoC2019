from itertools import groupby

RANGE = map(str, range(353096, 843212 + 1))

possible_passwords_1 = tuple(
    filter(
        # all digits increasing or constant and at least one group longer than one
        lambda psw: all(x <= y for x, y in zip(psw[:-1], psw[1:])) and any(len(list(g)) > 1 for _, g in groupby(psw)),
        RANGE
    )
)
possible_passwords_2 = tuple(
    filter(lambda psw: any(len(list(g)) == 2 for _, g in groupby(psw)), possible_passwords_1)
)

print(f'{len(possible_passwords_1)=}, {len(possible_passwords_2)=}')
