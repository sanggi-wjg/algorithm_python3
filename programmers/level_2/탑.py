# def find(heights, cur):
#     reverse = list(reversed([h for h in heights]))
#
#     for n, r in enumerate(reverse):
#         if cur < r:
#             print('[+]', cur, r, n)
#             return len(heights) - n
#         else:
#             print('[-]', cur, r, n)
#
#     return 0
#
#
# def solution(heights):
#     answer = []
#
#     while True:
#         if not heights:
#             break
#         cur = heights.pop()
#         answer.append(find(heights, cur))
#
#     return list(reversed(answer))

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
