x = 0
y = 0

with open('day02/input.txt', 'r') as input_file:
    for line in input_file:
        command, value = line.rstrip().split(' ')
        if command == 'forward':
            x += int(value)
        elif command == 'down':
            y += int(value)
        elif command == 'up':
            y -= int(value)

print(x, y)
print(x * y)
