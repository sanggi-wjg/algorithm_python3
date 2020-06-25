import sys

word = sys.stdin.readline().strip()

if word == ''.join(reversed(word)):
    sys.stdout.writelines('1')
else:
    sys.stdout.writelines('0')
