def solution(cacheSize, cities):
    answer = 0
    cache = []
    for i in range(len(cities)):
        # cache hit
        if cities[i].lower() in cache:
            cache.pop(cache.index(cities[i].lower()))
            cache.append(cities[i].lower())
            answer += 1
        # cache miss
        else:
            if len(cache) == cacheSize and cache:
                cache.pop(0)
                cache.append(cities[i].lower())
            else:
                if cacheSize == 0:
                    pass
                else:
                    cache.append(cities[i].lower())     
            answer += 5       
    return answer

'''
테스트 1 〉통과 (0.01ms, 10.3MB)
테스트 2 〉통과 (0.01ms, 10.2MB)
테스트 3 〉통과 (0.01ms, 10.1MB)
테스트 4 〉통과 (0.02ms, 10MB)
테스트 5 〉통과 (0.01ms, 10.3MB)
테스트 6 〉통과 (0.01ms, 10.1MB)
테스트 7 〉통과 (0.01ms, 10.2MB)
테스트 8 〉통과 (0.02ms, 10.2MB)
테스트 9 〉통과 (0.01ms, 10.1MB)
테스트 10 〉통과 (0.05ms, 10.1MB)
테스트 11 〉통과 (121.49ms, 17.4MB)
테스트 12 〉통과 (0.05ms, 10.2MB)
테스트 13 〉통과 (0.08ms, 10MB)
테스트 14 〉통과 (0.12ms, 10MB)
테스트 15 〉통과 (0.19ms, 10.1MB)
테스트 16 〉통과 (0.42ms, 10.2MB)
테스트 17 〉통과 (0.21ms, 10.3MB)
테스트 18 〉통과 (0.53ms, 10.2MB)
테스트 19 〉통과 (0.67ms, 10.3MB)
테스트 20 〉통과 (0.84ms, 10.2MB)
'''