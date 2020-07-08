import sys


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    l = round(n ** 0.5) + 1
    for i in range(3, l, 2):
        if n % i == 0:
            return False

    return True


M, N = map(int, sys.stdin.readline().split())
for i in range(M, N + 1):
    if is_prime(i): print(i)
