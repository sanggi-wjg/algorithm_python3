"""
ASCII
a = 97
"""
import sys

R, M, SUBTRACT = 31, 1234567891, 96

L = int(sys.stdin.readline())
text = list(sys.stdin.readline().strip())

result = sum([(ord(text[i]) - SUBTRACT) * (31 ** i) for i in range(L)]) % M
sys.stdout.writelines(str(result))
