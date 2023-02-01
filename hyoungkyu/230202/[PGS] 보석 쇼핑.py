def solution(gems):
    answer = []
    gems_set = list(set(gems))
    start = 0
    end = -1
    tmp = {}
    
    while True:
        # 조건 만족 X => 끝점 이동
        if len(tmp) != len(gems_set):
            end += 1
            if end < len(gems):
                if gems[end] not in tmp:
                    tmp[gems[end]] = 0
                tmp[gems[end]] += 1
                
        # 조건 만족 O => 시작점 이동
        elif len(tmp) == len(gems_set):
            answer.append([end-start, start+1, end+1])
            tmp[gems[start]] -= 1
            if tmp[gems[start]] == 0:
                del tmp[gems[start]]
            start += 1
            
        # 종료 조건
        if start == len(gems) or end == len(gems):
            break
            
    answer.sort()
    return answer[0][1:]

'''
정확성  테스트
테스트 1 〉통과 (0.03ms, 10.1MB)
테스트 2 〉통과 (0.11ms, 10.2MB)
테스트 3 〉통과 (0.36ms, 10.2MB)
테스트 4 〉통과 (0.49ms, 10.4MB)
테스트 5 〉통과 (0.90ms, 10.1MB)
테스트 6 〉통과 (0.01ms, 10.2MB)
테스트 7 〉통과 (0.02ms, 10.3MB)
테스트 8 〉통과 (1.23ms, 10.2MB)
테스트 9 〉통과 (1.89ms, 10.2MB)
테스트 10 〉통과 (0.86ms, 10.3MB)
테스트 11 〉통과 (0.79ms, 10.5MB)
테스트 12 〉통과 (2.08ms, 10.3MB)
테스트 13 〉통과 (4.64ms, 10.6MB)
테스트 14 〉통과 (2.37ms, 10.6MB)
테스트 15 〉통과 (5.68ms, 10.9MB)

효율성  테스트
테스트 1 〉통과 (7.27ms, 11.1MB)
테스트 2 〉통과 (8.45ms, 11.3MB)
테스트 3 〉통과 (21.52ms, 13.8MB)
테스트 4 〉통과 (10.44ms, 12MB)
테스트 5 〉통과 (32.53ms, 16.1MB)
테스트 6 〉통과 (48.68ms, 17MB)
테스트 7 〉통과 (48.27ms, 18.7MB)
테스트 8 〉통과 (62.09ms, 19.7MB)
테스트 9 〉통과 (66.28ms, 22MB)
테스트 10 〉통과 (76.19ms, 23MB)
테스트 11 〉통과 (83.38ms, 23.7MB)
테스트 12 〉통과 (41.15ms, 15.8MB)
테스트 13 〉통과 (66.05ms, 19.7MB)
테스트 14 〉통과 (283.51ms, 32.5MB)     *
테스트 15 〉통과 (123.49ms, 32MB)
'''