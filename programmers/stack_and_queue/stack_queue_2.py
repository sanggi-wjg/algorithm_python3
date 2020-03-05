def solution(bridge_length: int, weight: int, trucks: list):
    trucks.reverse()
    second = 0
    bridge = [0] * bridge_length

    while bridge:
        second += 1
        bridge.pop(0)

        if trucks:
            if weight >= sum(bridge) + trucks[-1]:
                bridge.append(trucks.pop())
            else:
                bridge.append(0)

    return second


testData = [
    [2, 10, [7, 4, 5, 6]],
    [100, 100, [10]],
    [100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, ]],
]

for b, w, t in testData:
    ans = solution(b, w, t)
    print(ans)

# for i in range(len(truck_weights)):
#     current_weight += truck_weights[-(i + 1)]
#     if weight >= current_weight:
#         can_drive_count += 1
#     else:
#         break
#
# for i in range(can_drive_count):
#     truck_weights.pop()
