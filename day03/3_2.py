n = 0
data = []

with open('day03/input.txt', 'r') as input_file:
    for line in input_file:
        data.append(line.rstrip())

# oxygen generator rating
oxygen_data = [x for x in data]
n_number = len(oxygen_data[0])

# iterate through digits
for i in range(n_number):
    sum_d = sum([int(n[i]) for n in oxygen_data])
    len_d = len(oxygen_data)
    res_d = '1' if sum_d * 2 >= len_d else '0'
    oxygen_data = [n for n in oxygen_data if n[i] == res_d]
    if len(oxygen_data) == 1:
        break

# CO2 scrubber rating
co2_data = [x for x in data]
n_number = len(co2_data[0])

# iterate through digits
for i in range(n_number):
    sum_d = sum([int(n[i]) for n in co2_data])
    len_d = len(co2_data)
    res_d = '1' if sum_d * 2 < len_d else '0'
    co2_data = [n for n in co2_data if n[i] == res_d]
    if len(co2_data) == 1:
        break


# binary to decimal
def binary_to_decimal(binary: str) -> int:
    res = 0
    multiplier = 1
    for b in reversed(binary):
        res += int(b) * multiplier
        multiplier <<= 1
    return res


oxygen_generator_rating = binary_to_decimal(oxygen_data[0])
co2_scrubber_rating = binary_to_decimal(co2_data[0])
print(oxygen_generator_rating * co2_scrubber_rating)
