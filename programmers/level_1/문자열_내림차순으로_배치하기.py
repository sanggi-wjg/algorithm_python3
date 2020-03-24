def solution(s: str):
    return ''.join(sorted(list(s), key = ord, reverse = True))


if __name__ == '__main__':
    test = [
        "Zbcdefg",
    ]

    for a in test:
        print(solution(a))
