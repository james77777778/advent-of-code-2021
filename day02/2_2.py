x = 0
y = 0
aim = 0

with open('day02/input.txt', 'r') as input_file:
    for line in input_file:
        command, value = line.rstrip().split(' ')
        if command == 'forward':
            x += int(value)
            y += aim * int(value)
        elif command == 'down':
            aim += int(value)
        elif command == 'up':
            aim -= int(value)

print(x, y)
print(x * y)
