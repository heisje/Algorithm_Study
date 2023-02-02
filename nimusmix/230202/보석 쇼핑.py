from collections import Counter

def solution(gems):
    ans = []
    kinds = len(set(gems))
    counter = Counter()

    start = 0
    for end in range(len(gems)):
        counter[gems[end]] += 1
        end += 1
        
        while len(counter) == kinds:
            counter[gems[start]] -= 1
            if counter[gems[start]] == 0:
                del counter[gems[start]]
            start += 1
            ans.append([start, end])

    return sorted(ans, key = lambda x: (x[1]-x[0], x[0]))[0]


# 정확성  테스트
# 테스트 1 〉	통과 (0.04ms, 10.2MB)
# 테스트 2 〉	통과 (0.13ms, 10.3MB)
# 테스트 3 〉	통과 (0.33ms, 10.4MB)
# 테스트 4 〉	통과 (0.27ms, 10.1MB)
# 테스트 5 〉	통과 (1.28ms, 10.1MB)
# 테스트 6 〉	통과 (0.02ms, 10.1MB)
# 테스트 7 〉	통과 (0.04ms, 10.3MB)
# 테스트 8 〉	통과 (0.45ms, 10.3MB)
# 테스트 9 〉	통과 (0.98ms, 10.4MB)
# 테스트 10 〉	통과 (0.69ms, 10.2MB)
# 테스트 11 〉	통과 (0.61ms, 10.1MB)
# 테스트 12 〉	통과 (1.62ms, 10.5MB)
# 테스트 13 〉	통과 (2.23ms, 10.4MB)
# 테스트 14 〉	통과 (1.23ms, 10.4MB)
# 테스트 15 〉	통과 (5.04ms, 11.2MB)

# 효율성  테스트
# 테스트 1 〉	통과 (5.84ms, 11.4MB)
# 테스트 2 〉	통과 (7.47ms, 11.5MB)
# 테스트 3 〉	통과 (19.90ms, 14.4MB)
# 테스트 4 〉	통과 (7.86ms, 11.9MB)
# 테스트 5 〉	통과 (31.03ms, 16.6MB)
# 테스트 6 〉	통과 (38.25ms, 18MB)
# 테스트 7 〉	통과 (44.00ms, 19.8MB)
# 테스트 8 〉	통과 (49.10ms, 20.8MB)
# 테스트 9 〉	통과 (59.58ms, 23.4MB)
# 테스트 10 〉	통과 (72.40ms, 24.6MB)
# 테스트 11 〉	통과 (75.24ms, 25.5MB)
# 테스트 12 〉	통과 (30.77ms, 16MB)
# 테스트 13 〉	통과 (50.99ms, 20.2MB)
# 테스트 14 〉	통과 (122.71ms, 35.2MB)
# 테스트 15 〉	통과 (118.70ms, 34.8MB)