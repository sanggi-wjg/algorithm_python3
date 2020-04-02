def solution(heights: list):
    answer, length = [], len(heights)
    heights.reverse()
    # print(heights)

    for i in range(length):
        h, isFlag = heights[i], False

        for j in range(i + 1, length, +1):
            if h < heights[j]:
                answer.append(length - j)
                isFlag = True
                break

        if not isFlag:
            answer.append(0)

    answer.reverse()
    return answer


if __name__ == '__main__':
    test = [
        # [6, 9, 5, 7, 4],
        [3, 9, 9, 3, 5, 7, 2],
        # [1, 5, 3, 6, 7, 6, 5]
    ]

    for a in test:
        print(solution(a))
