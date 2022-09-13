from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()

def bfs():
    queue = deque()
    queue.append(1)
    visited[1] = 0
    
    while queue:
        s = queue.popleft()
        
        if s == 100:
            return visited[100]
        
        for i in range(1, 7):
            w = s+i
            if adjList[w]: w = adjList[w][0]
            if visited[w] == -1:
                queue.append(w)
                visited[w] = visited[s] + 1

adjList = [[] for _ in range(106)]
visited = [-1 for _ in range(106)]
N, M = map(int, input().split())
for _ in range(N+M):
    a, b = map(int, input().split())
    adjList[a].append(b)
    
print(bfs())