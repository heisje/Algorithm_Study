from collections import deque

def bfs(start, goal):
    global visited
    queue = deque()
    queue.append(start)
    visited[start] = 0
    
    while queue:
        v = queue.popleft()
        
        if v == goal:
            return visited[v]
        
        for w in adjList[v]:
            if visited[w] == -1:
                queue.append(w)
                visited[w] = visited[v] + 1

N, K = map(int, input().split())
adjList = deque([] for _ in range(111111))
visited = [-1] * 111111

for i in range(111111):
    if 0 <= i-1 <= 111110: adjList[i].append(i-1)
    if 0 <= i+1 <= 111110: adjList[i].append(i+1)
    if 0 <= i*2 <= 111110: adjList[i].append(i*2)
    
print(bfs(N, K))