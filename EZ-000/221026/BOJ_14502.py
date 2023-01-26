import sys
from copy import deepcopy
from collections import deque
input = lambda: sys.stdin.readline().rstrip()


def bfs(r, c, visited):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    que = deque([(r, c)])
    while que:
        nr, nc = que.popleft()
        for idx in range(4):
            tr = nr + dr[idx]
            tc = nc + dc[idx]
            if (0 <= tr < N) and (0 <= tc < M) and not visited[tr][tc]:
                visited[tr][tc] = 2
                que.append((tr, tc))


def ncr(n, r, s, arr):
    if r == 0:
        new_walls.append(comb[:])
    else:
        for idx in range(s, n - r + 1):
            comb[r - 1] = arr[idx]
            ncr(n, r - 1, idx + 1, arr)


N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

walls = []
virus = []
saves = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            walls.append((i, j))
        elif board[i][j] == 2:
            virus.append((i, j))
        else:
            saves.append((i, j))

new_walls = []
comb = [0, 0, 0]
ncr(len(saves), 3, 0, saves)

max_cnt = 0
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for new_wall in new_walls:
    check = deepcopy(board)
    for i, j in new_wall:
        check[i][j] = 1
    for row, col in virus:
        bfs(row, col, check)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if check[i][j] == 0:
                cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)
