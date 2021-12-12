with open('day01/input.txt', 'r') as input_file:
    measurements = [int(line.rstrip()) for line in input_file]

prev_sum = 0
curr_sum = 0

count = 0
for i in range(len(measurements) - 2):
    curr_sum = measurements[i] + measurements[i + 1] + measurements[i + 2]
    if curr_sum > prev_sum:
        count += 1
    prev_sum = curr_sum

print(count - 1)
