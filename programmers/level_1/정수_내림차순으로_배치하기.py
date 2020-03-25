# def solution(n):
#     answer = [p for p in str(n)]
#     answer.sort(reverse = True)
#     return int(''.join(answer))


if __name__ == '__main__':
    test = [
        118372, 118371
    ]

    for a in test:
        print(solution(a))
