import collections
import sys

N = int(sys.stdin.readline())
number_cards = list(sys.stdin.readline().split())
number_cards = collections.Counter(number_cards)
M = int(sys.stdin.readline())
find_cards = list(sys.stdin.readline().split())

result = []
for i in range(M):
    if find_cards[i] in number_cards:
        result.append(number_cards.get(find_cards[i]))
    else:
        result.append(0)

sys.stdout.writelines(str(r) + ' ' for r in result)
