import sys

T = int(sys.stdin.readline())


def solution(h, w, n):
    a = n // h + 1
    b = n % h
    if b == 0:
        a -= 1
        b = h

    sys.stdout.writelines('%d%02d\n' % (b, a))


for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    solution(H, W, N)
