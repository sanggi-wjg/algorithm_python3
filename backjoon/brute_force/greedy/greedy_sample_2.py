# [(weight, value), ...]
DATA_LIST = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]
CAPACITY = 30


def get_max_value(data_list, capacity):
    # 가치순 정렬
    data_list = sorted(data_list, key = lambda x: x[1] / x[0], reverse = True)
    total_value, details = 0, []

    for weight, value in data_list:
        # 수용량이 남아 있다... 담자.
        if capacity - weight >= 0:
            capacity -= weight
            total_value += value
            details.append([weight, value, 1])

        # 수용량이 부족하다... 물건을 쪼개자.
        else:
            fraction = capacity / weight
            total_value += value * fraction
            details.append([weight * fraction, value * fraction, fraction])
            break

    return total_value, details


result = get_max_value(DATA_LIST, CAPACITY)
print(result)
