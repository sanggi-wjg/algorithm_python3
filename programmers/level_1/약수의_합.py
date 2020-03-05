def solution(n):
    answer = 0

    for i in range(1, n + 1):
        if n % i == 0:
            answer += i

    return answer


test = [
    12, 5
]

for t in test:
    print(solution(t))
