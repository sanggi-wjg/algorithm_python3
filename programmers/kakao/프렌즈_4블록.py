from pprint import pprint

direction = [(0, 0), (0, 1), (1, 0), (1, 1)]
move_direction = [(0, -1), (-1, -1), (0, -2), (-1, -2)]


def count_nearby(i: int, j: int, board: list) -> int:
    count = 0

    for x, y in direction:
        if board[i][j] == board[i + x][j + y]:
            count += 1

    return count


def move_block(i: int, j: int, board: list) -> list:
    for x, y in move_direction:
        board[i]

    return board


def solution(m: int, n: int, board: list):
    """
    :param m: 높이
    :param n: 너비
    :param board 보드
    """
    answer = 0

    board = list(map(list, board))

    for i in range(m - 1):
        for j in range(n - 1):
            if count_nearby(i, j, board) == 4:
                board = move_block(i, j, board)

            pprint(board)

    return answer


#  라이언(R), 무지(M), 어피치(A), 프로도(F), 네오(N), 튜브(T), 제이지(J), 콘(C)
sample = [
    # [4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"], 14],
    [6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"], 15],
]

for a, b, c, d in sample:
    r = solution(a, b, c)
    print('Equal /' if r == d else 'Not Equal /', r, '/', d, '\n')
