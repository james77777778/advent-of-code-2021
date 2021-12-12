from typing import List


def parse_numbers_and_boards(lines: List[str]):
    drawn_numbers = lines[0].rstrip().split(',')

    boards = []
    i = 2
    while i < len(lines):
        board = [[0 for _ in range(5)] for _ in range(5)]
        for j in range(5):
            numbers = lines[i + j].rstrip().split(' ')
            numbers = [x for x in numbers if x != '']
            for k, n in enumerate(numbers):
                board[j][k] = n
        boards.append(board)
        i += 6

    return drawn_numbers, boards


with open('day04/input.txt', 'r') as input_file:
    lines = input_file.readlines()

drawn_numbers, boards = parse_numbers_and_boards(lines)


def check_bingo(board, i, j) -> bool:
    row_res = True
    col_res = True
    # check row
    for k in range(5):
        if board[i][k] != 'x':
            row_res = False
            break
    # check col
    for k in range(5):
        if board[k][j] != 'x':
            col_res = False
            break
    return row_res or col_res


def get_sum_board(board, drawn_number) -> int:
    res = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] != 'x':
                res += int(board[i][j])
    return res * drawn_number


def bingo_for_board(board, drawn_number):
    for i in range(5):
        for j in range(5):
            if board[i][j] == drawn_number:
                board[i][j] = 'x'
                if check_bingo(board, i, j):
                    return board, True
    return board, False


# start bingo
for drawn_number in drawn_numbers:
    remove_idx = []
    # draw x of drawn_number
    for board_idx in range(len(boards)):
        board = boards[board_idx]
        boards[board_idx], is_bingo = bingo_for_board(board, drawn_number)
        if is_bingo:
            print(get_sum_board(board, int(drawn_number)))
            remove_idx.append(board_idx)
    # remove bingo boards
    for i in reversed(remove_idx):
        del boards[i]
