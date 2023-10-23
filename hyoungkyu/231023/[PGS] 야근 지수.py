# Lv3
import heapq

def solution(n, works):
    answer = 0
    pque = []
    for work in works:
        heapq.heappush(pque, -work)
        
    while pque and n > 0:
        num = -heapq.heappop(pque)
        if num > 0:
            num -= 1
            n -= 1
            heapq.heappush(pque, -num)
        # print(pque)
    for num in pque:
        answer += num * num
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.02ms, 10MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.19ms, 10.1MB)
테스트 9 〉	통과 (0.28ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.1MB)
테스트 13 〉	통과 (0.01ms, 10MB)

효율성  테스트
테스트 1 〉	통과 (451.93ms, 10.3MB)
테스트 2 〉	통과 (866.73ms, 10.4MB)
'''