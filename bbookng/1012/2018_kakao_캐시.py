def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.upper()         # 대소문자 구분안하니까 다 대문자로 통일

        if len(cache) < cacheSize:  # DB가 캐시 사이즈만큼 안찼을 때
            if city not in cache:   # 캐시에 없으면
                cache.append(city)  # 추가하고
                answer += 5         # 실행시간 + 5
            else:                   # 있으면
                cache.remove(city)  # 제거하고
                cache.append(city)  # 다시 뒤에 넣기
                answer += 1         # 실행시간 + 1

        else:                       # 캐시 사이즈 이상이라 알고리즘에 따라 적용시킬 때
            if city not in cache:   # DB에 없으면
                cache.append(city)  # 추가하고
                cache.pop(0)        # 제일 앞에 있는 거 빼고
                answer += 5         # 실행시간 + 5
            else:                   # 있으면
                cache.remove(city)  # 빼고
                cache.append(city)  # 뒤에 다시 넣고
                answer += 1         # 실행시간 + 1


    return answer

print(solution(5, ['jeju', 'pangyo', 'seoul', 'newyork', 'la', 'sanfrancisco', 'seoul', 'rome', 'paris', 'jeju', 'newyork', 'rome']))

'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.4MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.07ms, 10.4MB)
테스트 11 〉	통과 (80.38ms, 17.5MB)
테스트 12 〉	통과 (0.03ms, 10.3MB)
테스트 13 〉	통과 (0.11ms, 10.3MB)
테스트 14 〉	통과 (0.09ms, 10.2MB)
테스트 15 〉	통과 (0.12ms, 10.2MB)
테스트 16 〉	통과 (0.17ms, 10.2MB)
테스트 17 〉	통과 (0.26ms, 10.2MB)
테스트 18 〉	통과 (0.62ms, 10.3MB)
테스트 19 〉	통과 (0.76ms, 10.3MB)
테스트 20 〉	통과 (0.68ms, 10.3MB)
'''