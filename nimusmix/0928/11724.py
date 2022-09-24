from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()

def bfs(x):
    global cnt
    queue = deque()
    queue.append(x)
    visited[x] = 1
    
    while queue:
        i = queue.popleft()
        for j in adjList[i]:
            if visited[j] == 0:
                queue.append(j)
                visited[j] = 1
                cnt -= 1
                
    for ydx, y in enumerate(visited):
        if not y and adjList[ydx]:
            bfs(ydx)
            break
        
N, M = map(int, input().split())
adjList = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
cnt = N

for _ in range(M):
    u, v = map(int, input().split())
    adjList[u].append(v)
    adjList[v].append(u)

for x in range(N+1):
    if adjList[x]:
        bfs(x)
        break
    
print(cnt)