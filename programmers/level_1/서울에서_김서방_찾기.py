def solution(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))


test = [
    ["Jane", "Kim"]
]

for t in test:
    print(solution(t))
