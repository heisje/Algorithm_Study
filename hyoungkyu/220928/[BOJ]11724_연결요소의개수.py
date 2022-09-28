# 실버2 / 928ms
import sys
input = lambda:sys.stdin.readline().strip()

def DFS(v, N):
    stack = [0] * (N+1)
    top = -1
    visited[v] = 1
    while True:
        for w in dic[v]:
            if visited[w] == 0:
                top += 1
                stack[top] = v
                v = w
                visited[v] = 1
                break
        else:
            if top != -1:
                v = stack[top]
                top -= 1
            else:
                break


N, M = map(int, input().split())
dic = {i:[] for i in range(1, N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)
cnt = 0
visited = [0] * (N+1)
for i in dic:
    if not visited[i]:
        DFS(i, N)
        cnt += 1
print(cnt)