def solution(s: str, n: int):
    answer = ''

    for no in range(len(s)):
        if s[no] != ' ':
            asci = ord(s[no])

            if s[no].istitle() and asci + n > 90:
                temp = asci + n - 90
                asci = 64

            elif s[no].islower() and asci + n > 122:
                temp = asci + n - 122
                asci = 96

            else:
                temp = n

            answer += chr(asci + temp)

        else:
            answer += ' '

    return answer


if __name__ == '__main__':
    test = [
        ["AB", 1],
        ["z", 1],
        ["a B z", 4],
        ["a b c", 25],
        ["a b c d e f g h i j k l m n o p  q r s t u v w x y z", 25],
    ]

    for a, b in test:
        print(solution(a, b))
