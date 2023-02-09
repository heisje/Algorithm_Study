from collections import deque
from heapq import heappush, heappop
# def solution(stones, k):
#     answer = 0
#
#
#
#     dq = deque()
#     before = 200000000                      # 이전의 값
#     lowest = 200000000                      # 최소치
#
#     for i in range(len(stones)):
#
#         # print(dq)
#         # print(before)
#         # print(lowest)
#         # print("-------")
#         if stones[i] <= before:             # 작아지는 구간
#             if len(dq) < k:
#                 dq.append(stones[i])        # 큐가 덜 찼으므로 더 넣어줘도된다.
#             else:
#                 temp = dq.popleft()         # 큐가 k 보다 커지면 안되므로 빼낸다.
#                 if temp < lowest:
#                     lowest = temp
#                 dq.append(stones[i])
#
#         else:                               # 커지는 구간을 만나면
#             if len(dq) == k:                # 만약 큐가 가득차있다면 충분한 간격이 존재한다는 뜻이므로 큐의 가장 앞 값을 빼내서 최소치와 비교
#                 if dq[0] < lowest:
#                     lowest = dq[0]
#
#             dq.clear()
#
#         before = stones[i]
#     else:
#         if len(dq) == k:
#             if dq[0] < lowest:
#                 lowest = dq[0]
#
#
#     answer = lowest
#     return answer
#
#

# def solution(stones, k):
#
#     lowest = 200000000
#     dq = deque([])
#     for i in range(len(stones)):
#         if len(dq) < k:
#             dq.append(stones[i])
#
#         else:
#             dq.popleft()
#             dq.append(stones[i])
#             tmp = max(dq)
#             if tmp < lowest:
#                 lowest = tmp
#     return lowest

"""
테스트 1 〉	실패 (0.00ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.04ms, 10.1MB)
테스트 6 〉	통과 (0.21ms, 10.2MB)
테스트 7 〉	통과 (1.02ms, 10.1MB)
테스트 8 〉	통과 (0.94ms, 10.2MB)
테스트 9 〉	통과 (1.66ms, 10.1MB)
테스트 10 〉	통과 (0.03ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.02ms, 10.1MB)
테스트 13 〉	통과 (0.04ms, 10.2MB)
테스트 14 〉	통과 (0.23ms, 9.94MB)
테스트 15 〉	통과 (0.62ms, 10.1MB)
테스트 16 〉	통과 (1.19ms, 10.1MB)
테스트 17 〉	통과 (3.21ms, 10.1MB)
테스트 18 〉	통과 (0.02ms, 10.2MB)
테스트 19 〉	통과 (0.04ms, 10.2MB)
테스트 20 〉	통과 (0.04ms, 10.1MB)
테스트 21 〉	통과 (0.35ms, 10.1MB)
테스트 22 〉	통과 (0.56ms, 10.2MB)
테스트 23 〉	통과 (1.01ms, 10.2MB)
테스트 24 〉	통과 (1.83ms, 10.1MB)
테스트 25 〉	통과 (0.08ms, 10.1MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	실패 (시간 초과)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
테스트 9 〉	실패 (시간 초과)
테스트 10 〉	실패 (시간 초과)
테스트 11 〉	실패 (시간 초과)
테스트 12 〉	실패 (시간 초과)
테스트 13 〉	실패 (시간 초과)
테스트 14 〉	실패 (시간 초과)
"""

def solution(stones, k):
    start = 0
    end = 200000000
    lowest = end

    while(start <= end):
        mid = (start + end) // 2  # ~번째로 건너는 사람이라고 생각하자
        # print(mid)
        count = 0
        for i in range(len(stones)):
            if mid > stones[i]:
                count += 1
                if count == k:
                    break
            else:
                count = 0
        else:                       # 무사히 다 돈다면 좀 더 높혀봐도 된다.
            start = mid + 1
            continue
                                    # 무사히 다 못 도니까 낮추자.
        end = mid - 1
        if lowest > mid:
            lowest = mid
            continue

    return lowest - 1               # 무사히 다도는 최대치



print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
print(solution([5, 4, 3, 2, 1], 3))
print(solution([1, 2, 3, 4, 5, 6], 4))


"""
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.4MB)
테스트 3 〉	통과 (0.04ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.05ms, 10.2MB)
테스트 6 〉	통과 (0.26ms, 10.3MB)
테스트 7 〉	통과 (0.57ms, 10.2MB)
테스트 8 〉	통과 (0.67ms, 10.2MB)
테스트 9 〉	통과 (0.66ms, 10.2MB)
테스트 10 〉	통과 (0.03ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.03ms, 10.3MB)
테스트 13 〉	통과 (0.06ms, 10.3MB)
테스트 14 〉	통과 (0.21ms, 10.1MB)
테스트 15 〉	통과 (0.62ms, 10.3MB)
테스트 16 〉	통과 (0.76ms, 10.3MB)
테스트 17 〉	통과 (1.06ms, 10.3MB)
테스트 18 〉	통과 (0.03ms, 10.3MB)
테스트 19 〉	통과 (0.04ms, 10.4MB)
테스트 20 〉	통과 (0.04ms, 10.2MB)
테스트 21 〉	통과 (0.25ms, 10.2MB)
테스트 22 〉	통과 (0.72ms, 10.2MB)
테스트 23 〉	통과 (0.49ms, 10.2MB)
테스트 24 〉	통과 (0.70ms, 10.2MB)
테스트 25 〉	통과 (0.02ms, 10.1MB)
효율성  테스트
테스트 1 〉	통과 (272.49ms, 18.7MB)
테스트 2 〉	통과 (367.45ms, 18.6MB)
테스트 3 〉	통과 (357.81ms, 18.5MB)
테스트 4 〉	통과 (192.41ms, 18.5MB)
테스트 5 〉	통과 (232.28ms, 18.5MB)
테스트 6 〉	통과 (235.81ms, 18.5MB)
테스트 7 〉	통과 (424.87ms, 18.6MB)
테스트 8 〉	통과 (457.93ms, 18.5MB)
테스트 9 〉	통과 (438.34ms, 18.5MB)
테스트 10 〉	통과 (422.58ms, 18.5MB)
테스트 11 〉	통과 (362.95ms, 18.5MB)
테스트 12 〉	통과 (407.64ms, 18.5MB)
테스트 13 〉	통과 (266.49ms, 18.7MB)
테스트 14 〉	통과 (232.39ms, 18.5MB)
"""