# 골드4 / 3460ms
import sys
from copy import deepcopy
input = lambda:sys.stdin.readline().strip()

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
unchecked = 0
CCTV = []
for i in range(N):
    for j in range(M):
        if office[i][j] == 0:
            unchecked += 1
        elif office[i][j] != 6:
            CCTV.append((i, j, office[i][j]))

D = [[-1, 0], [0, 1], [1, 0], [0, -1]]      # 12시 / 3시 / 6시 / 9시

def visible(idx, dir, tmp_cnt, tmp_visited):
    ci, cj = CCTV[idx][0], CCTV[idx][1]
    while True:
        ni, nj = ci+D[dir][0], cj+D[dir][1]
        if 0<=ni<N and 0<=nj<M and office[ni][nj] != 6:
            if office[ni][nj] == 0 and tmp_visited[ni][nj] == 0:
                tmp_visited[ni][nj] = 1
                tmp_cnt -= 1
            ci, cj = ni, nj
        else:
            return tmp_cnt

minV = unchecked
arr = [[0]*M for _ in range(N)]
def f(idx, cnt, visited):
    global minV

    if CCTV[idx][2] == 1:
        for dir in range(4):
            tmp_visited = deepcopy(visited)
            tmp_cnt = visible(idx, dir, cnt, tmp_visited)
            if idx+1 < len(CCTV):
                f(idx+1, tmp_cnt, tmp_visited)
            else:
                minV = min(tmp_cnt, minV)

    elif CCTV[idx][2] == 2:
        for dir in range(2):
            tmp_visited = deepcopy(visited)
            tmp_cnt = visible(idx, dir, cnt, tmp_visited)
            tmp_cnt = visible(idx, dir+2, tmp_cnt, tmp_visited)
            if idx+1 < len(CCTV):
                f(idx+1, tmp_cnt, tmp_visited)
            else:
                minV = min(tmp_cnt, minV)

    elif CCTV[idx][2] == 3:
        for dir in range(4):
            tmp_visited = deepcopy(visited)
            tmp_cnt = visible(idx, dir, cnt, tmp_visited)
            tmp_cnt = visible(idx, (dir+1)%4, tmp_cnt, tmp_visited)
            if idx+1 < len(CCTV):
                f(idx+1, tmp_cnt, tmp_visited)
            else:
                minV = min(tmp_cnt, minV)
    
    elif CCTV[idx][2] == 4:
        for dir in range(4):
            tmp_visited = deepcopy(visited)
            tmp_cnt = visible(idx, dir, cnt, tmp_visited)
            tmp_cnt = visible(idx, (dir+1)%4, tmp_cnt, tmp_visited)
            tmp_cnt = visible(idx, (dir+2)%4, tmp_cnt, tmp_visited)
            if idx+1 < len(CCTV):
                f(idx+1, tmp_cnt, tmp_visited)
            else:
                minV = min(tmp_cnt, minV)

    elif CCTV[idx][2] == 5:
        tmp_visited = deepcopy(visited)
        tmp_cnt = visible(idx, 0, cnt, tmp_visited)
        tmp_cnt = visible(idx, 1, tmp_cnt, tmp_visited)
        tmp_cnt = visible(idx, 2, tmp_cnt, tmp_visited)
        tmp_cnt = visible(idx, 3, tmp_cnt, tmp_visited)
        if idx+1 < len(CCTV):
            f(idx+1, tmp_cnt, tmp_visited)
        else:
            minV = min(tmp_cnt, minV)
if CCTV:
    f(0, unchecked, arr)
print(minV)

