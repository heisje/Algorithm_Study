# Lv3
from collections import deque

def solution(n, edge):
    answer = 0
    adjL = [[] for _ in range(n+1)]
    for a, b in edge:
        adjL[a].append(b)
        adjL[b].append(a)

    visited = [float('inf')] * (n+1)
    visited[0] = 0
    visited[1] = 0
    idx_lst = deque()
    idx_lst.append(1)

    while idx_lst:
        idx = idx_lst.popleft()
        for i in adjL[idx]:
            if visited[i] > visited[idx] + 1:
                visited[i] = visited[idx] + 1
                idx_lst.append(i)

    answer = visited.count(max(visited))
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.21ms, 10.2MB)
테스트 5 〉	통과 (0.75ms, 10.7MB)
테스트 6 〉	통과 (2.31ms, 10.9MB)
테스트 7 〉	통과 (35.07ms, 16.8MB)
테스트 8 〉	통과 (32.91ms, 20.4MB)
테스트 9 〉	통과 (34.73ms, 20MB)
'''