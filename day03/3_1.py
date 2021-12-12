n = 0
ones = [0 for _ in range(12)]

with open('day03/input.txt', 'r') as input_file:
    for line in input_file:
        n += 1
        for i, d in enumerate(line.rstrip()):
            if d == '0':
                ones[i] += 1

binary = [x > n / 2 for x in ones]

gamma_rate = 0
epsilon_rate = 0
multiplier = 1
for d in reversed(binary):
    gamma_rate += int(d) * multiplier
    epsilon_rate += int(not d) * multiplier
    multiplier <<= 1

print(gamma_rate * epsilon_rate)
