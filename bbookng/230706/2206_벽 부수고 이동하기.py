from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]

def bfs():
    visited[0][0][0] = 1

    q = deque()
    q.append((0, 0, 0))

    while q:
        x, y, state = q.popleft()

        if x == N-1 and y == M-1:
            return visited[x][y][state]

        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 1 and state == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    q.append((nx, ny, 1))
                elif board[nx][ny] == 0 and visited[nx][ny][state] == 0:
                    visited[nx][ny][state] = visited[x][y][state] + 1
                    q.append((nx, ny, state))
    return -1

print(bfs())
