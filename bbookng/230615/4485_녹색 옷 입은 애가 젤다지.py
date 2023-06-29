import heapq

tc = 0

while True:
    tc += 1
    N = int(input())
    if N == 0:
        break
    cave = [list(map(int, input().split())) for _ in range(N)]
    board = [[float('inf') for _ in range(N)] for _ in range(N)]

    q = []
    heapq.heappush(q, (cave[0][0], (0, 0)))
    board[0][0] = cave[0][0]

    while q:
        rp, (x, y) = heapq.heappop(q)

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if rp + cave[nx][ny] < board[nx][ny]:
                    board[nx][ny] = rp + cave[nx][ny]
                    heapq.heappush(q, (rp + cave[nx][ny], (nx, ny)))

    print(f'Problem {tc}: {board[N-1][N-1]}')
