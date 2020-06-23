import sys

N, K = map(int, sys.stdin.readline().split())
COIN_LIST = [int(sys.stdin.readline()) for _ in range(N)]


def min_coin_count(coin_list, value):
    coin_count, coin_list = 0, sorted(coin_list, reverse = True)

    for coin in coin_list:
        coin_num = value // coin
        coin_count += coin_num
        value -= coin_num * coin

    return coin_count


result = min_coin_count(COIN_LIST, K)
print(result)
