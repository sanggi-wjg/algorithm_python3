N = int(input())
numbers = []

for _ in range(N):
    numbers.append(int(input()))

numbers.sort()

for n in numbers:
    print(n)
