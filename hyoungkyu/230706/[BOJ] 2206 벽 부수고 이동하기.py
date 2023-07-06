# 골드3 / 2196ms
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Map = [list(input().strip()) for _ in range(N)]
visited = [[1000001] * M for _ in range(N)]

def BFS():
    D = ((0, 1), (0, -1), (1, 0), (-1, 0))
    # 벽 뚫기 전 visited
    visited_possible = [[0] * M for _ in range(N)]
    # 벽 뚫은 후 visited
    visited_impossible = [[0] * M for _ in range(N)]
    visited_possible[0][0] = 1
    queue = deque()
    queue.append((0, 0, True))  # i, j, 벽 뚫을 수 있으면 True, 못뚫으면 False
    while queue:
        ci, cj, is_possible = queue.popleft()
        if ci == N-1 and cj == M-1:
            return max(visited_possible[ci][cj], visited_impossible[ci][cj])
        for di, dj in D:
            ni, nj = ci+di, cj+dj
            # 벽 뚫을 수 있을 경우
            if is_possible:
                if 0<=ni<N and 0<=nj<M and not visited_possible[ni][nj]:
                    if Map[ni][nj] == '0':
                        visited_possible[ni][nj] = visited_possible[ci][cj]+1
                        queue.append((ni, nj, is_possible))
                    else:
                        visited_impossible[ni][nj] = visited_possible[ci][cj]+1
                        queue.append((ni, nj, False))
            # 못뚫을 경우
            else:
                if 0<=ni<N and 0<=nj<M and not visited_impossible[ni][nj] and Map[ni][nj] == '0':
                    visited_impossible[ni][nj] = visited_impossible[ci][cj]+1
                    queue.append((ni, nj, is_possible))


ans = BFS()
print(ans if ans else -1)

# def DFS():
#     D = ((0, 1), (0, -1), (1, 0), (-1, 0))
#     visited[0][0] = 1
#     stack = []
#     ci, cj, possible = 0, 0, True
#     while True:
#         for di, dj in D:
#             ni, nj = ci+di, cj+dj
#             if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 1000001:
#                 if Map[ni][nj] == '1' and possible:
#                     visited[ni][nj] = min(visited[ni][nj], visited[ci][cj] + 1)
#                     stack.append((ni, nj, False))
#                     break
#                 elif Map[ni][nj] == '0':
#                     visited[ni][nj] = min(visited[ni][nj], visited[ci][cj] + 1)
#                     stack.append((ni, nj, possible))
#                     break
#             elif ni == N-1 and nj == M-1:
#                 visited[ni][nj] = min((visited[ni][nj]), visited[ci][cj] + 1)
#         else:
#             if stack:
#                 ci, cj, possible = stack.pop()
#             else:
#                 return visited[N-1][M-1]

# ans = DFS()
# print(ans if ans != 1000001 else -1)
# for i in visited:
#     print(*i)