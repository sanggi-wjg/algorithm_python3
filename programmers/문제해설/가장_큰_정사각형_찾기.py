def solution(board):
    line, col = len(board), len(board[0])

    if line == 1 or col == 1:
        for i in range(line):
            for j in range(col):
                if board[i][j] == 1:
                    return 1

    for i in range(1, line):
        for j in range(1, col):
            if board[i][j] == 1:
                board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1

    answer = 0
    for b in board:
        line_max = max(b)
        if line_max > answer:
            answer = line_max

    return answer ** 2


sample = [
    [
        [0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1]
    ],
    [
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 0, 1, 0]
    ],  # 9
    # [
    #     [0, 0, 1, 1],
    #     [1, 1, 1, 1]
    # ],  # 4
    # [
    #     [1, 0, 1],
    #     [0],
    #     [1],
    # ]
]

for s in sample:
    a = solution(s)
    print(a)
