import math


def solution(n, m):
    return [math.gcd(n, m), int(n * m / math.gcd(n, m))]


if __name__ == '__main__':
    test = [
        [3, 12], [2, 5],
    ]

    for a, b in test:
        print(solution(a, b))
