def solution(arr, divisor):
    answer = [p for p in arr if p % divisor == 0]

    if answer:
        return sorted(answer)
    else:
        return [-1]


test = [
    [[5, 9, 7, 10], 5],
    [[2, 36, 1, 3], 1],
    [[3, 2, 6], 10]
]

for a, d in test:
    print(solution(a, d))
