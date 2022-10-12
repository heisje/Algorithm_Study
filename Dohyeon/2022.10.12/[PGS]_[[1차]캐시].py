def solution(cacheSize, cities):
    answer = 0
    cache_hit = 1
    cache_miss = 5
    used = 0
    cache = []
    for city in cities:
        city = city.upper()
        if used < cacheSize:
            for i in range(len(cache)):
                if cache[i] == city:
                    tmp = cache.pop(i)
                    cache.append(tmp)
                    answer += cache_hit
                    break
            else:
                cache.append(city)
                used += 1
                answer += cache_miss

        else:
            for i in range(cacheSize):
                if cache[i] == city:
                    tmp = cache.pop(i)
                    cache.append(tmp)
                    answer += cache_hit
                    break
            else:
                if cacheSize == 0:
                    answer += cache_miss
                else:
                    cache.pop(0)
                    cache.append(city)
                    answer += cache_miss

    return answer

C = 0
li = 	["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

print(solution(C, li))