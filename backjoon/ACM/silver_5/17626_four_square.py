from itertools import combinations

N = int(input())
calc_list, x = [], 1

while True:
    value = x ** 2
    if value > N:
        break

    calc_list.append(value)
    x += 1
"""
brute_force
"""
for i in range(1, len(calc_list) + 1):
    value_list = combinations(calc_list, i)
    value_list = sorted(value_list, reverse = True)

    for v in value_list:
        sum_value = sum(v)
        if sum_value == N:
            print(i)
            exit()
