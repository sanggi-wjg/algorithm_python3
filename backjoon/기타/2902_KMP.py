import sys

string = sys.stdin.readline().strip()
string_split = string.split('-')
# print(string_split)

result = ''
for word in string_split:
    result += word[0]

print(result)
