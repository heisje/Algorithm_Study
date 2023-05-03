import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(r)]

def bfs():
    visited = [[0] * c for _ in range(r)]
    q = deque([(0, 0)])
    visited[0][0] = 1
    cnt = 0

    while q:
        dr, dc = q.popleft()
        for x, y in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            nr, nc = dr + x, dc + y
            if 0 <= nr < r and 0 <= nc < c and not visited[nr][nc]:
                if board[nr][nc] == 0:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                elif board[nr][nc] == 1:
                    board[nr][nc] = 0
                    visited[nr][nc] = 1
                    cnt += 1
    return cnt

results = []
time = 0

while True:
    melted = bfs()
    time += 1
    if melted == 0:
        print(time-1)
        print(results[-1])
        break
    results.append(melted)




bfs()