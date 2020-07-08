import sys

while True:
    number = sys.stdin.readline().strip()
    if number == '0': break

    if number == ''.join(reversed(number)):
        sys.stdout.writelines('yes\n')
    else:
        sys.stdout.writelines('no\n')
