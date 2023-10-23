# 골드3 / 404ms
import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

# 0: 빈 칸, 1: 벽, 2: 바이러스
N, M = map(int, input().split())
lab = []
cnt = 0
virus_lst = []
visited = [[0] * N for _ in range(N)]
for i in range(N):
    tmp_input = list(map(int, input().split()))
    tmp_lab = []
    for j in range(N):
        tmp_lab.append(tmp_input[j])
        if tmp_input[j] == 0:
            cnt += 1
        elif tmp_input[j] == 1:
            visited[i][j] = -1
        elif tmp_input[j] == 2:
            visited[i][j] = 0
            virus_lst.append((i, j))
    lab.append(tmp_input)

def get_act_virus(virus_lst, act_virus, M):
    if len(virus_lst) <= M:
        act_virus.append(tuple(virus_lst))

    elif len(act_virus) < M:
        for comb in combinations(virus_lst, M):
            act_virus.append(tuple(comb))

    return act_virus

def bfs(lab, N, virus, cnt):
    que = deque()
    visited = [[0]*N for _ in range(N)]
    for act in virus:
        que.appendleft(act)
        visited[act[0]][act[1]] = 1
    tmp_que = deque()
    move = 0
    while que:
        ci, cj = que.popleft()
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and lab[ni][nj] != 1:
                visited[ni][nj] = visited[ci][cj] + 1
                tmp_que.append((ni, nj))
                if lab[ni][nj] == 0:
                    cnt -= 1
        if len(que) == 0 and len(tmp_que):
            move += 1
            if cnt == 0: break
            que = tmp_que
            tmp_que = deque()

    return move if cnt == 0 else float('inf')
                
act_virus = get_act_virus(virus_lst, [], M)

if cnt == 0: print(0)
else: 
    answer = float('inf')
    for act_vi in act_virus:
        answer = min(bfs(lab, N, act_vi, cnt), answer)
    print(answer if answer != float('inf') else -1)
