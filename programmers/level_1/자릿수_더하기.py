def solution(n):
    return sum([int(p) for p in str(n)])


if __name__ == '__main__':
    test = [
        "123",
        "987",
    ]

    for a in test:
        print(solution(a))
