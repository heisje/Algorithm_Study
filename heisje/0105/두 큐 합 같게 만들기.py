# https://school.programmers.co.kr/learn/courses/30/lessons/118667
from collections import deque
import copy

def solution(queue1, queue2):
    max_move = (len(queue1) + len(queue2)) * 2
    sum_q = sum(queue1 + queue2) // 2
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    dq = deque()
    dq.append(( sum(queue1), sum(queue2), 0))
    while dq:
        
        sum1, sum2, move = dq.popleft()
        if sum1 == sum_q and sum2 == sum_q:
            return move
        if move > max_move:
            break
        if sum1 > sum2:
            temp = queue1.popleft()
            queue2.append(temp)
            dq.append((sum1-temp, sum2+temp, move+1))
        if sum1 < sum2:
            temp = queue2.popleft()
            queue1.append(temp)
            dq.append((sum1+temp, sum2-temp, move+1))
    
    return -1

a = [3, 2, 7, 2]	
b = [4, 6, 5, 1]
print(solution(a,b))
a = [1, 2, 1, 2]	
b = [1, 10, 1, 2]
print(solution(a,b))
a = [1, 1]	
b = [1, 5]
print(solution(a,b))

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10.3MB)
# 테스트 5 〉	통과 (0.06ms, 10.3MB)
# 테스트 6 〉	통과 (0.04ms, 10.3MB)
# 테스트 7 〉	통과 (0.07ms, 10.3MB)
# 테스트 8 〉	통과 (0.03ms, 10.3MB)
# 테스트 9 〉	통과 (0.07ms, 10.3MB)
# 테스트 10 〉	통과 (0.17ms, 10.4MB)
# 테스트 11 〉	통과 (63.07ms, 14.7MB)
# 테스트 12 〉	통과 (9.41ms, 14.7MB)
# 테스트 13 〉	통과 (3.38ms, 12.3MB)
# 테스트 14 〉	통과 (4.05ms, 12.6MB)
# 테스트 15 〉	통과 (8.36ms, 18.3MB)
# 테스트 16 〉	통과 (5.80ms, 18.5MB)
# 테스트 17 〉	통과 (5.91ms, 17.7MB)
# 테스트 18 〉	통과 (19.25ms, 33.3MB)
# 테스트 19 〉	통과 (24.23ms, 37.5MB)
# 테스트 20 〉	통과 (65.04ms, 37.8MB)
# 테스트 21 〉	통과 (53.05ms, 37.9MB)
# 테스트 22 〉	통과 (90.98ms, 37.7MB)
# 테스트 23 〉	통과 (87.08ms, 37.9MB)
# 테스트 24 〉	통과 (95.05ms, 38.1MB)
# 테스트 25 〉	통과 (0.06ms, 10.1MB)
# 테스트 26 〉	통과 (0.04ms, 10.1MB)
# 테스트 27 〉	통과 (0.03ms, 10.2MB)
# 테스트 28 〉	통과 (126.67ms, 19.4MB)
# 테스트 29 〉	통과 (0.87ms, 10.8MB)
# 테스트 30 〉	통과 (70.52ms, 19.2MB)
