import sys

N = list(map(str, sys.stdin.readline().rstrip()))
# print(N)
N = sorted(N, reverse = True)
# print(N)
sys.stdout.writelines(''.join(N))
