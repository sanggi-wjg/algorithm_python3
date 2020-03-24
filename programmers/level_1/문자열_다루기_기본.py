def solution(s):
    return s.isdigit() and len(s) in [4, 6]


if __name__ == '__main__':
    test = [
        "a234",
        "1234",
        "12345",
    ]

    for a in test:
        print(solution(a))
