import sys
input = lambda: sys.stdin.readline().strip()

def bfs(start):
    global cnt
    visited = [-1] * (N+1)
    queue = []
    queue.append(start)
    visited[start] = 0

    while queue:
        v = queue.pop(0)
        for w in adjList[v]:
            if visited[w] == -1:
                queue.append(w)
                visited[w] = visited[v] + 1
    return visited

N, M = map(int, input().split())
adjList = [[] for _ in range(N+1)]
minV = N*N

for _ in range(M):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

li = []
for i in range(1, N+1):
    li.append(sum(bfs(i)))

print(li.index(min(li))+1)