import numpy as np

matrix = np.zeros((1000, 1000), dtype=np.uint8)


with open('day05/input.txt', 'r') as input_file:
    for line in input_file:
        points = line.rstrip().split(' -> ')  # ['x1,y1', 'x2,y2']
        x1, y1 = [int(x) for x in points[0].split(',')]
        x2, y2 = [int(x) for x in points[1].split(',')]

        if x1 == x2:
            y_step = 1 if y1 < y2 else -1
            for i in range(y1, y2 + y_step, y_step):
                matrix[x1][i] += 1
        elif y1 == y2:
            x_step = 1 if x1 < x2 else -1
            for i in range(x1, x2 + x_step, x_step):
                matrix[i][y1] += 1


def count_overlap(matrix):
    mask = matrix > 1
    return np.sum(mask)


print(count_overlap(matrix))
