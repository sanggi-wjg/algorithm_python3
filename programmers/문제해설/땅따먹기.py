def solution(land):
    if len(land) == 1:
        return max(land[0])

    dp = [[0, 0, 0, 0] for _ in range(len(land))]

    for i in range(len(land)):
        dp[i][0] = max(dp[i + 1][1], dp[i + 1][2], dp[i + 1][3]) + land[i][0]
        dp[i][1] = max(dp[i + 1][0], dp[i + 1][2], dp[i + 1][3]) + land[i][1]
        dp[i][2] = max(dp[i + 1][1], dp[i + 1][0], dp[i + 1][3]) + land[i][2]
        dp[i][3] = max(dp[i + 1][1], dp[i + 1][2], dp[i + 1][0]) + land[i][3]
        print(dp, '\n')

    return None


sample = [
    [
        [1, 2, 3, 5],
        [5, 6, 7, 8],
        [4, 3, 2, 1]
    ],  # 16
    [
        [1, 2, 3, 5],
    ]
]

for s in sample:
    a = solution(s)
    print(a)
