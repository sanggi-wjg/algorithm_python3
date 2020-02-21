def find(heights, cur):
    reverse = list(reversed([h for h in heights]))

    for n, r in enumerate(reverse):
        if cur < r:
            print('[+]', cur, r, n)
            return len(heights) - n
        else:
            print('[-]', cur, r, n)

    return 0


def solution(heights):
    answer = []

    while True:
        if not heights:
            break
        cur = heights.pop()
        answer.append(find(heights, cur))

    return list(reversed(answer))


if __name__ == '__main__':
    testData = [
        [6, 9, 5, 7, 4],
        [3, 9, 9, 3, 5, 7, 2],
        [1, 5, 3, 6, 7, 6, 5],
    ]

    for test in testData:
        ans = solution(test)
        print(ans, end = '\n\n')
