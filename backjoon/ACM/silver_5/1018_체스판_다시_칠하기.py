"""
W로 시작하는 보드판, B로 시작하는 보드판을
모두 생성해서 비교
"""
from pprint import pprint


def get_base_board(a, b, num = 8):
    board = []
    for i in range(num):
        temp = []
        for j in range(num):
            if i % 2 == 0:
                temp.append(a) if j % 2 == 0 else temp.append(b)
            else:
                temp.append(b) if j % 2 == 0 else temp.append(a)
        board.append(temp)

    return board


N, M = map(int, input().split())
BOARD = [input() for _ in range(N)]
W_BOARD, B_BOARD = get_base_board('W', 'B'), get_base_board('B', 'W')

wb_count, bb_count = [], []
pprint(BOARD[0:8][0:8])

for n in range(N - 7):
    TEMP_BOARD = []
    temp = BOARD[n:n + 8]
    for m in range(M - 7):
        TEMP_BOARD.append(temp[m:m + 8])

    B = []
    for tb in TEMP_BOARD:
        B.append(list(tb))

    for board, wb_board, bb_board in zip(B, W_BOARD, B_BOARD):
        w_count, b_count = 0, 0
        for b, wb, bb in zip(board, wb_board, bb_board):
            if b != wb:
                w_count += 1
            if b != bb:
                b_count += 1
        wb_count.append(w_count)
        bb_count.append(bb_count)
