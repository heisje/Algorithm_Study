# 골드4 / 5924ms
import sys
input = lambda:sys.stdin.readline().strip()
from collections import deque

f = ['D', 'S', 'L', 'R']
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    visited = [0] *10000
    queue = deque()
    visited[A] = ''
    queue.append(A)            # 출력하기 위한 문자열 s도 같이 큐에 추가
    while queue:                    # BFS -> 한 값에 대해 DSLR 다 돌리기
        n = queue.popleft()
        if n == B:
            print(visited[n])
            break
        
        var = n
        # D
        tmp = (2*var) % 10000
        if visited[tmp] == 0:
            visited[tmp] = visited[var] + 'D'
            queue.append(tmp)

        # S
        tmp = var-1 if var>0 else 9999
        if visited[tmp] == 0:
            visited[tmp] = visited[var] + 'S'
            queue.append(tmp)

        # L
        tmp = (var % 1000) * 10 + (var // 1000)
        if visited[tmp] == 0:
            visited[tmp] = visited[var] + 'L'
            queue.append(tmp)

        # R
        tmp = (var % 10) * 1000 + (var // 10)
        if visited[tmp] == 0:
            visited[tmp] = visited[var] + 'R'
            queue.append(tmp)
        
