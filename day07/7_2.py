from collections import defaultdict


def sum_of_sequence(k: int) -> int:
    if k == 0:
        return 0
    return (1 + k) * k // 2


crabs = defaultdict(int)

with open('day07/input.txt', 'r') as input_file:
    for line in input_file:
        res = [int(n) for n in line.rstrip().split(',')]
        for n in res:
            crabs[n] += 1

min_fuel = 1024 * 1024 * 1024 * 1024  # very big number
i = 0
for i in range(max(crabs.keys())):
    fuel = 0
    for k, v in crabs.items():
        fuel += sum_of_sequence(abs(k - i)) * v
    if fuel > min_fuel:
        break
    min_fuel = min(min_fuel, fuel)

print(i, min_fuel)
