import sys
from collections import deque
input = sys.stdin.readline

delta = [(-1, 0), (1, 0), (0, -1), (1, 0)]      # 상하좌우
def bfs(r, c):
    q = [(r, c)]
    for d in range(4):
        nr = r + delta[d][0]
        nc = c + delta[d][1]
        if nr < N + 1 and nc < N + 1:
            q.append((nr, nc))


N = int(input())
for _ in range(N):
    space = [list(map(int, input().split())) for _ in range(N)]
    size = 2

