import sys
from collections import deque
from copy import deepcopy
input = lambda:sys.stdin.readline()

# 아이디어 : 일단 bfs를 돌려서, 변하는(유의미한) 0의 위치를 찾고. 이 0의 위치들을 조합으로 선택하여
#            선택을 다 해보았다면, bfs를 돌려본다. 그리고 최대값을 찾는다.

dt = (
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
)

# 0이 들어갈 세가지를 조합으로 찾아서, 찾은 뒤 bfs로 다 확인해본다.
def dfs(z_n, zero_visited):
    global max_result
    if len(zero_visited) == 3:
        new_grid = deepcopy(grid)
        new_grid[zero_arr[zero_visited[0]][1]][zero_arr[zero_visited[0]][0]] = 1
        new_grid[zero_arr[zero_visited[1]][1]][zero_arr[zero_visited[1]][0]] = 1
        new_grid[zero_arr[zero_visited[2]][1]][zero_arr[zero_visited[2]][0]] = 1
        dq = deepcopy(startdq)
        while dq:
            x, y = dq.popleft()
            for d in dt:
                go_x = x + d[0]
                go_y = y + d[1]
                if 0 <= go_x < M and 0 <= go_y < N:
                    if new_grid[go_y][go_x] == 0:
                        new_grid[go_y][go_x] = 2
                        dq.append((go_x, go_y))
        result = 0
        for n in range(N):
            result += new_grid[n].count(0)
        if max_result < result:
            max_result = result
        #print(result)
        return
    if z_n == Z_NUM:  # 숫자가 넘어갈 경우 break
        return
    # 아래를 포함시키는 것 으로 dfs
    dfs(z_n+1, zero_visited + [z_n])
    # 아래를 포함시키지 않는 것으로 dfs
    dfs(z_n+1, zero_visited)

    
# 아이디어: 변환될 수 있는 2가 될 위치를 전부 다 찾고, 조합으로 구현한다.
N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

dq = deque()
startdq = deque()
for n in range(N):
    for m in range(M):
        if grid[n][m] == 2:
            dq.append((m, n))
            startdq.append((m, n))

new_grid = deepcopy(grid)
zero_arr = []
while dq:
    x, y = dq.popleft()
    for d in dt:
        go_x = x + d[0]
        go_y = y + d[1]
        if 0 <= go_x < M and 0 <= go_y < N:
            if new_grid[go_y][go_x] == 0:
                new_grid[go_y][go_x] = 2
                dq.append((go_x, go_y))
                zero_arr.append((go_x, go_y))

# zero_arr로 순열을 만들어서 grid와 Z_NUM로 계속 0의 개수를 세본다.
Z_NUM = len(zero_arr)
max_result = 0
dfs(0, [])
print(max_result)

# 골드4 / 80분 / 3964ms
