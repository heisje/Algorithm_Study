import sys
from collections import deque
input = sys.stdin.readline

def bfs(A):
    q = deque()
    q.append([A, ''])
    while q:
        tmp, method = q.popleft()
        if tmp == B:                                # A 가 B 가 되면
            return method                           # 정답 반환

        D = (tmp * 2) % 10000                       # D, S, L, R 계산한 값 만들어주고
        S = tmp - 1 if tmp != 0 else 9999
        L = (tmp % 1000) * 10 + (tmp // 1000)
        R = (tmp % 10) * 1000 + (tmp // 10)

        for i in [D, S, L, R]:                      # for 문에서 순회
            if i == D and not visited[D]:           # 각 값이 해당 되고 방문한 적 없으면
                q.append([D, method+'D'])           # 큐에 명령 실행시킨 값과 문자열에 명령 추가
                visited[D] = 1                      # 방문처리
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

