# def solution(num):
#     return "Odd" if num % 2 != 0 else "Even"


# def solution(arr):
#     return sum(arr) / len(arr)

# def solution(arr: list):
#     arr.remove(min(arr))
#     return arr if len(arr) > 0 else [-1]


# def solution(phone_number):
#     return '*' * (len(phone_number) - 4) + phone_number[-4:]

# def solution(arr1, arr2):
#     answer = []
#
#     for i in range(len(arr1)):
#         temp = []
#         for j in range(len(arr1[i])):
#             temp.append(arr1[i][j] + arr2[i][j])
#         answer.append(temp)
#     return answer
def solution(a, b):
    for i in range(b):
        for j in range(a):
            print('*', end = '')
        print()


if __name__ == '__main__':
    test = [
        # 10, 11,

        # [1, 2, 3, 4], [5, 5]

        # [4, 3, 2, 1], [10], [5, 1, 2, 6, 8]

        # "01033334444", "027778888"

        # [[[1, 2], [2, 3]], [[3, 4], [5, 6]]],        [[[1], [2]], [[3], [4]]]
        [5, 3]
    ]

    # for a in test:
    #     print(solution(a))

    for a, b in test:
        print('ans', solution(a, b))
