import sys
from collections import deque
input = sys.stdin.readline

def bfs(A):
    q = deque()
    q.append([A, ''])
    while q:
        tmp, method = q.popleft()
        if tmp == B:
            return method
        D = (tmp * 2) % 10000
        S = tmp - 1 if tmp != 0 else 9999
        L = (tmp % 1000) * 10 + (tmp // 1000)
        R = (tmp % 10) * 1000 + (tmp // 10)

        for i in [D, S, L, R]:
            if i == D and not visited[D]:
                q.append([D, method+'D'])
                visited[D] = 1
            elif i == S and not visited[S]:
                q.append([S, method + 'S'])
                visited[S] = 1
            elif i == L and not visited[L]:
                q.append([L, method + 'L'])
                visited[L] = 1
            elif i == R and not visited[R]:
                q.append([R, method + 'R'])
                visited[R] = 1


T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    visited = [0] * 10001
    print(bfs(A))

