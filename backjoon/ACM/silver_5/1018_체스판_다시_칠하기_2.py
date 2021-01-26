"""
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW

10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB
"""

N, M = map(int, input().split())
BOARD = [input() for _ in range(N)]


def make_board(first_char, second_char):
    board = []
    for i in range(8):
        text = ''
        for j in range(8):
            if i % 2 == 0:
                if j % 2 == 0:
                    text += first_char
                else:
                    text += second_char
            else:
                if j % 2 == 0:
                    text += second_char
                else:
                    text += first_char
        board.append(text)

    return board


WHITE_FIRST_BOARD = make_board('W', 'B')
BLACK_FIRST_BOARD = make_board('B', 'W')
WHITE_COUNT, BLACK_COUNT = [], []

for x in range(N - 7):
    for y in range(M - 7):
        white_cnt, black_cnt = 0, 0

        for i in range(8):
            for j in range(8):
                word = BOARD[i + x][j + y]
                white = WHITE_FIRST_BOARD[i][j]
                black = BLACK_FIRST_BOARD[i][j]

                if word != white:
                    white_cnt += 1

                if word != black:
                    black_cnt += 1

        WHITE_COUNT.append(white_cnt)
        BLACK_COUNT.append(black_cnt)

print(min(min(WHITE_COUNT), min(BLACK_COUNT)))
