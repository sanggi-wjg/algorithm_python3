def solution(num: int):
    answer = 0
    while True:
        if num == 1:
            break
        elif answer >= 500:
            return -1

        num = num / 2 if num % 2 == 0 else num * 3 + 1
        answer += 1

    return answer


if __name__ == '__main__':
    test = [
        6, 16, 626331
    ]

    for a in test:
        print(solution(a))
