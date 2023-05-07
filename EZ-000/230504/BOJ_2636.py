import sys
from copy import deepcopy

input = lambda: sys.stdin.readline().rstrip()

def bfs(board):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visited = {(0, 0)}
    melted = set()
    queue = [(0, 0)]
    while queue:
        nr, nc = queue.pop(0)
        if board[nr][nc]:
            melted.add((nr, nc))
            continue
        for d in range(4):
            fr, fc = nr + dr[d], nc + dc[d]
            if (fr, fc) not in visited and -1 < fr and -1 < fc and fr < R and fc < C:
                queue.append((fr, fc))
                visited.add((fr, fc))

    for r, c in list(melted):
        board[r][c] = 0
    
    return board

R, C = map(int, input().split())
board = []

for _ in range(R):
    board.append(list(map(int, input().split())))

cnt = 0
while True:
    cheese = sum([sum(x) for x in board])
    if not cheese:
        break
    cnt += 1
    old_board = deepcopy(board)
    board = bfs(deepcopy(board))

print(cnt)
print(sum([sum(x) for x in old_board]))
