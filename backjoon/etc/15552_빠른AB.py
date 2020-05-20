import sys

T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    sys.stdout.writelines(str(A + B) + '\n')
