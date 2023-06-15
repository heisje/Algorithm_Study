import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y, thief, lost_rupees):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        i, j = queue.popleft()
        for d in range(4):
            ni = i + direction[d][0]
            nj = j + direction[d][1]
            
            if 0 <= ni < N and 0 <= nj < N:
                if lost_rupees[ni][nj] > lost_rupees[i][j] + thief[ni][nj]:
                    lost_rupees[ni][nj] = lost_rupees[i][j] + thief[ni][nj]
                    queue.append((ni, nj))

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
problem_cnt = 1
while True:
    N = int(input())
    if N == 0:
        break
    
    thief = [list(map(int, input().split())) for _ in range(N)]
    lost_rupees = [[1e9] * N for _ in range(N)]
    lost_rupees[0][0] = thief[0][0]
    
    bfs(0, 0, thief, lost_rupees)
    print(f'Problem {problem_cnt}: {lost_rupees[N-1][N-1]}')
    problem_cnt += 1