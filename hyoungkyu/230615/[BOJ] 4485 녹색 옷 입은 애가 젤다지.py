# from collections import deque       # BFS - 632ms
import heapq                        # 다익스트라 - 168ms

tc = 0
while True:
    tc += 1
    N = int(input())
    if N == 0: break

    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[float("INF")] * N for _ in range(N)]
    visited[0][0] = arr[0][0]

    answer = 0
    D = ((0, 1), (1, 0), (0, -1), (-1, 0))      # 우하좌상
    # que = deque()
    hq = []
    heapq.heappush(hq, (arr[0][0], 0, 0))

    # que.append((0, 0))

    # while que:
    while hq:
        # ci, cj = que.popleft()
        value, ci, cj = heapq.heappop(hq)
        if ci == N-1 and cj == N-1: break
        for di, dj in D:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and value + arr[ni][nj] < visited[ni][nj]:
                visited[ni][nj] = value + arr[ni][nj]
                heapq.heappush(hq, (value + arr[ni][nj], ni, nj))
                # que.append((ni, nj))

    print(f'Problem {tc}: {visited[N-1][N-1]}')