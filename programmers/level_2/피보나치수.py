def solution(n):
    terms = [0, 1]
    i = 2
    while i <= n:
        terms.append(terms[i - 1] + terms[i - 2])
        i = i + 1

    return (terms[-2] + terms[-3]) % 1234567


test = [
    3, 5,
    1000,
    # 99999,
    # 100000
]

for t in test:
    ans = solution(t)
    print(ans)
