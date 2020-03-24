def solution(s):
    s = s.lower()
    return True if s.count('p') == s.count('y') else False


if __name__ == '__main__':
    test = [
        "pPoooyY",
        "Pyy",
        "PPP"
    ]

    for a in test:
        print(solution(a))
