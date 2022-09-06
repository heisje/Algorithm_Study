from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()

M, N, H = map(int, input().split())
garage = [list(map(int, input().split())) for _ in range(N) for _ in range(H)]

k_li = range(1, H+1)
visited = [[-1] * M for _ in range(N) for _ in range(H)]
queue = deque()

for i in range(N*H):
    for j in range(M):
        if garage[i][j] == 1:
            queue.append((i, j))
            visited[i][j] = 0
            
while queue:
    x, y = queue.popleft()
    
    if 0 <= y-1 and visited[x][y-1] == -1 and garage[x][y-1] == 0:
        queue.append((x, y-1))
        visited[x][y-1] = visited[x][y] + 1
    if y+1 < M and visited[x][y+1] == -1 and garage[x][y+1] == 0:
        queue.append((x, y+1))
        visited[x][y+1] = visited[x][y] + 1
    if N*k_li[x//N]-N <= x-1 and visited[x-1][y] == -1 and garage[x-1][y] == 0:
        queue.append((x-1, y))
        visited[x-1][y] = visited[x][y] + 1
    if x+1 <= N*k_li[x//N]-1 and visited[x+1][y] == -1 and garage[x+1][y] == 0:
        queue.append((x+1, y))
        visited[x+1][y] = visited[x][y] + 1
    if 0 <= x-N and visited[x-N][y] == -1 and garage[x-N][y] == 0:
        queue.append((x-N, y))
        visited[x-N][y] = visited[x][y] + 1
    if x+N < N*H and visited[x+N][y] == -1 and garage[x+N][y] == 0:
        queue.append((x+N, y))
        visited[x+N][y] = visited[x][y] + 1

maxV = 0
flag = 1

for i in range(N*H):
    for j in range(M):
        if garage[i][j] == 0 and visited[i][j] == -1: flag = 0

for t in visited:
    if maxV < max(t): maxV = max(t)
    
print(maxV if flag else -1)