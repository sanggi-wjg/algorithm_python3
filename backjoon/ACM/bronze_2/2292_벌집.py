"""
1  7   19   37  61
 +6 +12 +18   +24
"""
import sys

N = int(sys.stdin.readline())
increase, count = 1, 1
while True:
    # print(increase, count)
    if increase >= N:
        break
    increase += 6 * count
    count += 1

sys.stdout.writelines(str(count))
