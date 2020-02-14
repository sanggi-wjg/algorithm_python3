def solution(genres, plays):
    answer = []
    total = dict()
    origin = list()

    for n in range(len(genres)):
        if genres[n] in total.keys():
            total.__setitem__(genres[n], total.get(genres[n]) + plays[n])
        else:
            total.__setitem__(genres[n], plays[n])

        origin.append({ 'genre': genres[n], 'plays': plays[n], 'idx': n })

    priorityKey = dict(sorted(total.items(), key = lambda x: x[1], reverse = True)).keys()
    # print(total)
    # print(priorityKey)
    # print(origin)
    origin = sorted(origin, key = lambda x: x['plays'], reverse = True)
    # print(origin)

    for key in priorityKey:
        cnt = 0
        for n, o in enumerate(origin):
            # print("key : {} , cnt : {} , o : {} , n : {}".format(key, cnt, o, n))
            if key == o.get('genre'):
                answer.append(o.get('idx'))
                cnt += 1

            if cnt == 2:
                break

    return answer


if __name__ == '__main__':
    ans = solution(
        ["classic", "pop", "classic", "classic", "pop"],
        [500, 600, 150, 800, 2500]
    )
    print(ans)
