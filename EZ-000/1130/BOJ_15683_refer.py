import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline


def check(arr, r, c, d):
    for dr, dc in d:
        nr, nc = r, c
        while True:
            nr += dr
            nc += dc
            if nr < 0 or nc < 0 or N <= nr or M <= nc:
                break
            if arr[nr][nc] == 6:
                break
            elif arr[nr][nc] == 0:
                arr[nr][nc] = '#'


def dfs(arr):
    global cnt
    global mini
    if cnt == cctv_cnt:
        temp = 0
        for i in range(n):
            temp += arr[i].count(0)
        mini = min(mini, temp)
        return
    # while True:


N, M = map(int, input().split())
office = []
for _ in range(N):
    office.append(list(map(int, input().split())))

U = (-1, 0)
D = (1, 0)
L = (0, -1)
R = (0, 1)
CCTV = {1: [[U], [D], [L], [R]],
        2: [[U, D], [L, R]],
        3: [[U, R], [R, D], [D, L], [L, U]],
        4: [[U, L, R], [D, L, R], [L, U, D], [R, U, D]],
        5: [[U, D, L, R]]}

camQ = deque([])
locQ = deque([])
for n in range(N):
    for m in range(M):
        if office[n][m] in [1, 2, 3, 4, 5]:
            camQ.append(office[n][m])
            locQ.append((n, m))

cctv_cnt = len(camQ)
cnt = 0
mini = 0
que = []
dfs()

check(office, 1, 1, CCTV[2][1])
