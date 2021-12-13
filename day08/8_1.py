res = 0
with open('day08/input.txt', 'r') as input_file:
    for line in input_file:
        raw_patterns, raw_digits = line.rstrip().split(' | ')
        digits = raw_digits.split(' ')
        for d in digits:
            if len(d) == 2 or len(d) == 4 or len(d) == 3 or len(d) == 7:  # 1, 4, 7, 8
                res += 1

print(res)
