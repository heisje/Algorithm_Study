from collections import defaultdict

def solution(info, query):
    ans = []    
    cases = defaultdict(list)

    for candidate in info:
        candidate = candidate.split()
        for lang in [candidate[0], '-']:
            for field in [candidate[1], '-']:
                for career in [candidate[2], '-']:
                    for food in [candidate[3], '-']:
                        cases[lang + field + career + food].append(int(candidate[4]))

    for key in cases.keys():
        cases[key].sort()

    for q in query:
        q = q.replace(' and ', '')
        q, score = q.split()
        score = int(score)
        conditioned = cases[q]

        tmp = l = len(conditioned)
        low, high = 0, l-1
        
        while low <= high:
            mid = (low + high) // 2
            
            if score <= conditioned[mid]:
                tmp = mid
                high = mid - 1
            else:
                low = mid + 1

        ans.append(l - tmp)
            
    return ans


# 정확성  테스트
# 테스트 1 〉	통과 (0.21ms, 10.4MB)
# 테스트 2 〉	통과 (0.36ms, 10.2MB)
# 테스트 3 〉	통과 (0.29ms, 10.3MB)
# 테스트 4 〉	통과 (1.02ms, 10.4MB)
# 테스트 5 〉	통과 (1.83ms, 10.4MB)
# 테스트 6 〉	통과 (5.41ms, 10.4MB)
# 테스트 7 〉	통과 (2.24ms, 10.6MB)
# 테스트 8 〉	통과 (50.66ms, 11.2MB)
# 테스트 9 〉	통과 (43.83ms, 13MB)
# 테스트 10 〉	통과 (43.76ms, 13.7MB)
# 테스트 11 〉	통과 (1.87ms, 10.5MB)
# 테스트 12 〉	통과 (6.23ms, 10.3MB)
# 테스트 13 〉	통과 (2.40ms, 10.7MB)
# 테스트 14 〉	통과 (31.36ms, 12MB)
# 테스트 15 〉	통과 (21.77ms, 11.9MB)
# 테스트 16 〉	통과 (1.85ms, 10.2MB)
# 테스트 17 〉	통과 (4.73ms, 10.5MB)
# 테스트 18 〉	통과 (21.66ms, 11.9MB)

# 효율성  테스트
# 테스트 1 〉	통과 (795.22ms, 61MB)
# 테스트 2 〉	통과 (797.05ms, 60.9MB)
# 테스트 3 〉	통과 (819.57ms, 60.6MB)
# 테스트 4 〉	통과 (824.57ms, 61.3MB)


# 원래 풀었던 코드
# def check(score, condition, candidate):
#     if score > int(candidate[4]):
#         return 0
    
#     if condition == candidate[:4]:
#         return 1
    
#     if '-' not in condition:
#         return 0
    
#     for n in range(4):
#         if condition[n] == '-':
#             continue
#         elif condition[n] != candidate[n]:
#             return 0
#     return 1

# def solution(info, query):
#     ans = [0] * len(query)
#     candidates = [i.split() for i in info]
    
#     for idx, i in enumerate(query):
#         condition = i.split(' and ')
#         food, score = condition[-1].split()
#         score = int(score)
#         condition[-1] = food
        
#         for candidate in candidates:
#             ans[idx] += check(score, condition, candidate)
#     return ans
