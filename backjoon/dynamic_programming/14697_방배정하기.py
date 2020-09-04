import sys
from itertools import permutations

room1, room2, room3, num_people = map(int, sys.stdin.readline().split())
room_list = [room1, room2, room3]
room_list.reverse()


def count_room(rooms: list, num_people: int) -> int:
    for room in rooms:
        if num_people % room == 0:
            return 1

    rooms = permutations(rooms)
    for room in rooms:
        print(room, num_people % room[0], (num_people % room[0]) % room[1])
        if ((num_people % room[0]) % room[1]) % room[2] == 0:
            return 1

    return 0


result = count_room(room_list, num_people)
print(result)

"""
5 9 12 113
=> 1

3 6 9 112
=> 0

2 3 4 101

48 49 50 1
"""

# sample = [3, 49, 50]
# print(sample)
# for n in range(490, 501):
#     result = solution(sample, n)
#     print('num of people:', n, '/', result, '\n')
