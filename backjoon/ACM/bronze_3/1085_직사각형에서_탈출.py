x, y, w, h = map(int, input().split())

print(min(w - x, h - y, abs(0 - x), abs(0 - y)))
