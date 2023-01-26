def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        answer += 5 * len(cities)
    else:
        cache = [''] * cacheSize
        for city in cities:
            city = city.lower()
            for idx in range(cacheSize):
                if cache[idx] == city:
                    answer += 1
                    del cache[idx]
                    cache.append(city)
                    break
            else:
                cache.pop(0)
                cache.append(city)
                answer += 5
    return answer
