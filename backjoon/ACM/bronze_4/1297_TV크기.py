import math
import sys

diagonal_line, height_ratio, width_ratio = map(int, sys.stdin.readline().split())
result = math.sqrt((diagonal_line * diagonal_line) / ((height_ratio * height_ratio) + (width_ratio * width_ratio)))
print(int(result * height_ratio), int(result * width_ratio))
