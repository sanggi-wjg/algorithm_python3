import math
import sys

N, K = map(int, sys.stdin.readline().split())
result = int(math.factorial(N) / (math.factorial(N - K) * math.factorial(K)))
sys.stdout.writelines(str(result))
