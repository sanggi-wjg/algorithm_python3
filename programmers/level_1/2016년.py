from datetime import datetime


def solution(a, b):
    return ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'][datetime(2016, a, b).weekday()]


test = [
    [5, 24]
]

for i, j in test:
    print(solution(i, j))
