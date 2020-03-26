def solution(x, n):
    return [x * (i + 1) for i in range(n)]


if __name__ == '__main__':
    test = [
        [2, 5], [4, 3], [-4, 2]
    ]

    for a, b in test:
        print(solution(a, b))
