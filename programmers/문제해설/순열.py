def solution(arr):
    if len(arr) <= 1:
        return True

    arr = sorted(arr)

    for i in range(1, len(arr)):
        if arr[i - 1] + 1 != arr[i]:
            return False

    return True


sample = [
    [5, 4, 2],
    [5, 5, 5],
    [4, 1, 3, 2],
    [4, 1, 3],
]

for s in sample:
    a = solution(s)
    print(a)
