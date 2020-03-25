# def solution(num):
#     return "Odd" if num % 2 != 0 else "Even"


def solution(arr):
    return sum(arr) / len(arr)


if __name__ == '__main__':
    test = [
        [1, 2, 3, 4],
        [5, 5]
    ]

    for a in test:
        print(solution(a))
