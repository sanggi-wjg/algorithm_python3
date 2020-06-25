import sys

numbers = map(int, sys.stdin.readline().split())
number_list = []

for number in numbers:
    number_list.append(number * number)

print(sum(number_list) % 10)
