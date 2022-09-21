import sys
import heapq

input = lambda :sys.stdin.readline().strip()

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def solution(i, j, di, dj):
    q = []

    heapq.heappush(q, (-arr[i][j], i, j))
    heapq.heappush(q, (-arr[i+di][j+dj], i+di, j+dj))
    visited = []
    candidates = []
    tmp = 0

    for _ in range(2):
        value, ci, cj = heapq.heappop(q)
        tmp -= value
        visited.append((ci, cj))

        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and (ni, nj) not in visited and (-arr[ni][nj], ni, nj) not in q:
                heapq.heappush(candidates, (-arr[ni][nj], ni, nj))

    for _ in range(2):
        value, ci, cj = heapq.heappop(candidates)
        tmp -= value
        visited.append((ci, cj))

        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and (ni, nj) not in visited and (-arr[ni][nj], ni, nj) not in q:
                heapq.heappush(candidates, (-arr[ni][nj], ni, nj))

    return tmp

answer = 0
for i in range(N-1):
    for j in range(M-1):
        answer = max(answer, solution(i, j, 1, 0))
        answer = max(answer, solution(i, j, 0, 1))

print(answer)

