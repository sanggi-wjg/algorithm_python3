def solution(n):
    for i in range(n):
        num, sum = str(i), i

        for j in range(len(num)):
            sum += int(num[j])

        if sum == n:
            return i

    return 0


# 216 -> 198
N = int(input())
answer = solution(N)
print(answer)
