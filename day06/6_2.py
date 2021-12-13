from collections import defaultdict


fishes = defaultdict(int)
n_days = 256

with open('day06/input.txt', 'r') as input_file:
    for line in input_file:
        res = [int(n) for n in line.rstrip().split(',')]
        for n in res:
            fishes[n] += 1

for n in range(n_days):
    new_fishes = defaultdict(int)
    n_add = 0
    for k, v in fishes.items():
        if k > 0:
            new_fishes[k - 1] = v
        elif k == 0:
            n_add = v
            new_fishes[8] = v
    new_fishes[6] += n_add
    fishes = new_fishes

res = 0
for k, v in fishes.items():
    res += v
print(res)
