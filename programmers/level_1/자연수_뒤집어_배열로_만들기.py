def solution(n):
    answer = [int(p) for p in str(n)]
    answer.reverse()
    return answer


if __name__ == '__main__':
    test = [
        12345
    ]

    for a in test:
        print(solution(a))
