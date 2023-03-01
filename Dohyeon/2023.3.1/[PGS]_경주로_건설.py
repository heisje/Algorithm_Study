from collections import deque


def bfs(board, x, y, cost, d):  # 보드 크기, 좌표, 비용, 방향

    N = len(board)
    graph = [[0] * N for _ in range(N)]
    dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # 상좌하우

    for a in range(N):
        for b in range(N):
            if board[a][b] == 1:
                graph[a][b] = 1  # 벽

    q = deque()
    q.append((x, y, cost, d))

    while q:
        x, y, cost, direction = q.popleft()
        for i in range(len(dir)):
            new_x = x + dir[i][0]
            new_y = y + dir[i][1]

            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N:  # 보드 안이라는 조건
                continue
            if graph[new_x][new_y] == 1:                            # 벽이면 안됨
                continue

            if direction == i:          # 이전 방향과 같으면
                newcost = cost + 100
            else:
                newcost = cost + 600

            if graph[new_x][new_y] == 0 or ((graph[new_x][new_y] != 0) and graph[new_x][new_y] > newcost):  # 간적 없거나 더 싼 비용이 가능할 경우
                q.append((new_x, new_y, newcost, i))
                graph[new_x][new_y] = newcost

            else:
                continue

    return graph[N - 1][N - 1]

def solution(board):

    return min(bfs(board, 0, 0, 0, 2), bfs(board, 0, 0, 0, 3))