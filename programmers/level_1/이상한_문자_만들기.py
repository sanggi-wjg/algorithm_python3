def solution(s: str):
    answer = ''

    for word in list(s.split(' ')):
        temp = list(word)

        for n, w in enumerate(temp):
            temp[n] = temp[n].lower() if (n + 1) % 2 == 0 else temp[n].upper()

        answer += '{} '.format(''.join(temp))

    return answer[:len(answer) - 1]


if __name__ == '__main__':
    test = [
        "try hello world",
        "tRY hELLo world",
        "123",
        "sp ace",
    ]

    for a in test:
        print("@" + solution(a) + "@")
