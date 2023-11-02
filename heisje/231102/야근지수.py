import heapq

def solution(n, works):
    works = list(map(lambda x : -x ,works))
    
    heapq.heapify(works)
    
    while works and n:
        temp = heapq.heappop(works) + 1
        if temp == 1:
            break
        n -= 1
        heapq.heappush(works, temp)
    
    return sum([x**2 for x in works])

# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.02ms, 10.1MB)
# 테스트 5 〉	통과 (0.02ms, 10.1MB)
# 테스트 6 〉	통과 (0.02ms, 10.1MB)
# 테스트 7 〉	통과 (0.01ms, 10.1MB)
# 테스트 8 〉	통과 (0.54ms, 10.2MB)
# 테스트 9 〉	통과 (0.72ms, 10.2MB)
# 테스트 10 〉	통과 (0.01ms, 10.1MB)
# 테스트 11 〉	통과 (0.02ms, 10MB)
# 테스트 12 〉	통과 (0.02ms, 10.1MB)
# 테스트 13 〉	통과 (0.02ms, 10.1MB)
# 효율성  테스트
# 테스트 1 〉	통과 (440.95ms, 10.2MB)
# 테스트 2 〉	통과 (414.45ms, 10.2MB)
# 채점 결과
# 정확성: 86.7
# 효율성: 13.3
# 합계: 100.0 / 100.0