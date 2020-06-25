import sys

text_list = []
result = ''

for _ in range(5):
    text_list.append(sys.stdin.readline().strip())

# 리스트 중 가장 긴 길이
for i in range(max(len(t) for t in text_list)):
    for text in text_list:
        result += text[i] if len(text) > i else ''

sys.stdout.writelines(result)
