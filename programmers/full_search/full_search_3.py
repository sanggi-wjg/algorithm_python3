def solution(baseball):
    answer = 0
    strike_dict = dict()
    ball_dict = dict()

    for num, strike, ball in baseball:
        if strike >= 1:
            pass
        if ball >= 1:
            pass

    return answer


if __name__ == '__main__':
    testData = [
        [
            [123, 1, 1],
            [356, 1, 0],
            [327, 2, 0],
            [489, 0, 1],
        ]
    ]

    for test in testData:
        ans = solution(test)
        print(ans)
