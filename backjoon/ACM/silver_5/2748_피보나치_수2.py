def fibonacci(num):
    fibo = [0, 1]

    for n in range(2, num + 1):
        fibo.append(fibo[n - 2] + fibo[n - 1])

    return fibo


N = int(input())
answer = fibonacci(N)
# print(answer)
print(answer[-1])
