from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())
art = [list(input()) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(i, j, c):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1
    
    while queue:
        x, y = queue.popleft()
        
        for n in range(4):
            nx = x + dx[n]
            ny = y + dy[n]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and art[nx][ny] == c:
                queue.append((nx, ny))
                visited[nx][ny] = 1

normal = 0
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            color = art[i][j]
            bfs(i, j, color)
            normal += 1

blind = 0
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if art[i][j] == 'G':
            art[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            color = art[i][j]
            bfs(i, j, color)
            blind += 1

print(normal, blind)