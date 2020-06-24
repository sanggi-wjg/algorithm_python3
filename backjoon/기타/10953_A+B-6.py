import sys

N = int(sys.stdin.readline())
for _ in range(N):
    A, B = map(int, sys.stdin.readline().split(','))
    sys.stdout.writelines(str(A + B) + '\n')
