import collections
import sys


def get_average(numbers):
    return int(round(sum(numbers) / len(numbers)))


def get_center_num(numbers):
    return numbers[int(len(numbers) / 2)]


def get_high_freq_num(numbers):
    counter = collections.Counter(numbers)
    most_common = counter.most_common(2)
    # print(counter, most_common)

    if len(most_common) == 1:
        return most_common[0][0]
    else:
        return most_common[0][0] if most_common[0][1] > most_common[1][1] else most_common[1][0]


def get_range(numbers):
    return numbers[-1] - numbers[0]


N = int(sys.stdin.readline())
numbers = []

for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

numbers = sorted(numbers)
# print(numbers)

sys.stdout.writelines(str(get_average(numbers)) + '\n')
sys.stdout.writelines(str(get_center_num(numbers)) + '\n')
sys.stdout.writelines(str(get_high_freq_num(numbers)) + '\n')
sys.stdout.writelines(str(get_range(numbers)) + '\n')
