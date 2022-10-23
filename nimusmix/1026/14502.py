import sys
from copy import deepcopy
from collections import deque
from itertools import combinations
input = lambda: sys.stdin.readline().strip()

def bfs(x, y):
    global new_cnt
    
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    
    while queue:
        i, j = queue.popleft()
        
        if new_cnt < safe_max:
            return
        
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and new_map[ni][nj] == 0:
                new_cnt -= 1
                visited[ni][nj] = 1
                new_map[ni][nj] = 2
                queue.append((ni, nj))

N, M = map(int, input().split())
the_map = [list(map(int, input().split())) for _ in range(N)]
empty, virus = [], []
safe_cnt = safe_max = 0

for i in range(N):
    for j in range(M):
        if the_map[i][j] == 0:
            safe_cnt += 1
            empty.append((i, j))
        elif the_map[i][j] == 2:
            virus.append((i, j))

for c in combinations(empty, 3):
    new_map = deepcopy(the_map)
    new_cnt = safe_cnt
    visited = [[0] * M for _ in range(N)]

    for i, j in c:
        new_map[i][j] = 1
        new_cnt -= 1
    
    for x, y in virus:
        bfs(x, y)

    if new_cnt > safe_max:
        safe_max = new_cnt

print(safe_max)