import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()


def bfs():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    que = deque([(0, 0, 0)])
    while que:
        row, col, flag = que.popleft()

        if row == N - 1 and col == M - 1:
            return visited[row][col][flag]

        for idx in range(4):
            nr, nc = row + dr[idx], col + dc[idx]
            if -1 < nr < N and -1 < nc < M:
                if not board[nr][nc] and not visited[nr][nc][flag]:
                    que.append((nr, nc, flag))
                    visited[nr][nc][flag] = visited[row][col][flag] + 1
                if board[nr][nc] and not flag:
                    que.append((nr, nc, 1))
                    visited[nr][nc][1] = visited[row][col][0] + 1

    return -1


N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
print(bfs())
