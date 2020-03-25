import re


def solution(dartResult):
    answer = list()

    splitList = re.findall('[0-9]+[A-Z][*#]?', dartResult)
    print(splitList)

    for no, item in enumerate(splitList):
        tmp = 0

        score = int(''.join(re.findall('[0-9]+', item)))
        sdt = ''.join(re.findall('[A-Z]+', item))
        option = ''.join(re.findall('[*#]', item))

        if sdt == 'S':
            tmp = score
        elif sdt == 'D':
            tmp = score * score
        elif sdt == 'T':
            tmp = score * score * score
        print('no:', no, '| score: ', score, '| sdt:', sdt, '| option:', option, '| tmp : ', tmp)

        if option == '*':
            tmp = tmp * 2
            if len(answer) >= 1:
                answer[no - 1] = answer[no - 1] * 2
        elif option == '#':
            tmp = int('-' + str(tmp))

        answer.append(tmp)
        print(answer)

    return sum(answer)


if __name__ == '__main__':
    test = [
        '1S2D*3T',
        '1D2S#10S',
        '1D2S0T',
        '1S*2T*3S',
        '1D2S3T*',
    ]

    for a in test:
        print(solution(a))
