import sys
from copy import deepcopy
from collections import deque
from itertools import combinations
input = lambda: sys.stdin.readline().strip()

def bfs(x, y):
    global safe_cnt
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    
    while queue:
        i, j = queue.popleft()
        
        if safe_cnt < safe_max:                                        # 안전지대의 수가 max보다 적으면 return
            return
        
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and new_map[ni][nj] == 0:
                safe_cnt -= 1                                          # 바이러스 감염시킬 수 있으면 안전지대의 수 -= 1
                visited[ni][nj] = 1
                queue.append((ni, nj))

N, M = map(int, input().split())
the_map = [list(map(int, input().split())) for _ in range(N)]
empty, virus = [], []                                                  # 빈 칸 리스트, 바이러스 리스트 생성
safe = safe_max = 0

for i in range(N):
    for j in range(M):
        if the_map[i][j] == 0:                                         # 빈 칸이면
            safe += 1                                                  # 초기 안전지대의 수 += 1
            empty.append((i, j))                                       # 빈 칸 리스트에 추가
        elif the_map[i][j] == 2:                                       # 바이러스면
            virus.append((i, j))                                       # 바이러스 리스트에 추가

for c in combinations(empty, 3):                                       # 조합 생성하고 순회
    new_map = deepcopy(the_map)                                        # 지도 deepcopy
    safe_cnt = safe                                                    # 초기 안전지대의 수를 새로운 변수에 복사
    visited = [[0] * M for _ in range(N)]                              # visited 생성

    for i, j in c:
        new_map[i][j] = 1                                              # 벽 세우기
        safe_cnt -= 1                                                  # 안전 지대의 수 -= 1
    
    for x, y in virus:
        bfs(x, y)

    if safe_cnt > safe_max:                                            # 안전지대의 수가 max보다 크다면
        safe_max = safe_cnt                                            # max를 현재 안전지대의 수로 변경

print(safe_max)