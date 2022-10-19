def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)

    cities = list(map(lambda x:x.capitalize(), cities))
    cache = []
    answer = idx = 0

    while len(cache) < cacheSize:
        target = cities[idx]
        if target in cache:
            answer += 1
            cache.pop(cache.index(target))
        else:
            answer += 5
        cache.append(target)
        idx += 1

    for i in range(idx, len(cities)):
        target = cities[i]
        if target in cache:
            answer += 1
            cache.pop(cache.index(target))
        else:
            answer += 5
            cache.pop(0)
        cache.append(target)

    return answer