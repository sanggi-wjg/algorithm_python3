def solution(n):
    answer = ''
    for i in range(n):
        answer = answer + '수' if i % 2 == 0 else answer + '박'

    return answer


test = [
    3, 4
]

for t in test:
    print(solution(t))
