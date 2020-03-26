import math


def solution(n):
    sqrt = math.sqrt(n)
    return int((sqrt + 1) * (sqrt + 1)) if sqrt.is_integer() else -1


if __name__ == '__main__':
    test = [
        121, 3
    ]

    for a in test:
        print(solution(a))
