def solution(x: int):
    return True if x % sum([int(p) for p in (str(x))]) == 0 else False


if __name__ == '__main__':
    test = [
        10, 12, 11, 13
    ]

    for a in test:
        print(solution(a))
