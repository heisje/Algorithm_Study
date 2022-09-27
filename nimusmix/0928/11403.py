from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()

def bfs(s):
    visited = [0] * N
    queue = deque()
    queue.append(s)
    
    while queue:
        v = queue.popleft()
        for w in adjList[v]:
            if visited[w] == 0:
                queue.append(w)
                visited[w] = 1
    return visited

N = int(input())
adjList = [[] for _ in range(N)]
ans = []

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j]:
            adjList[i].append(j)

for i in range(N):
    ans.append(bfs(i))
    
for j in ans:
    print(*j)