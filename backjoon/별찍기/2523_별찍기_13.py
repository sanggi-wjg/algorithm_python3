import sys

N = int(sys.stdin.readline())
temp = 0

for i in range(1, (N * 2)):
    if i > N: temp += 1
    print('*' * i if i < N else '*' * (N - temp))
