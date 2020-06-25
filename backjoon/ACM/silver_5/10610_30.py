import sys

N = sys.stdin.readline().strip()

if '0' not in N:
    sys.stdout.writelines('-1')
else:
    number_sum = 0

    for n in N:
        number_sum += int(n)

    if number_sum % 3 == 0:
        sys.stdout.writelines(sorted(list(N), reverse = True))
    else:
        sys.stdout.writelines('-1')

# 메모리 초과...
# N = int(sys.stdin.readline())
# N = list(str(N))
#
# permuted = permutations(N)
# permuted = sorted(set(map(tuple, permuted)), reverse = True)
#
# for p in permuted:
#     number = int(''.join(p))
#     if number % 30 == 0:
#         sys.stdout.writelines(str(number))
#         break
#     else:
#         sys.stdout.writelines('-1')
#         break
