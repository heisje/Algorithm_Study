import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def bfs(nx, ny):                                                    # 바이러스 퍼트리기
    q = deque()
    q.append((nx, ny))
    while q:
        si, sj = q.popleft()
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = si + di, sj + dj
            if 0 <= ni < N and 0 <= nj < M and not tmp[ni][nj]:
                tmp[ni][nj] = 2                                      # 바이러스 전파
                q.append((ni, nj))

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

comList = []                                                         # 벽 세울 좌표 조합을 담을 list
for i in range(N):
    for j in range(M):
        if not arr[i][j]:                                            # 벽도 아니고 바이러스도 아니면
            comList.append((i, j))                                   # 벽이 될 자격이 있으므로 추가

for com in combinations(comList, 3):                                 # 3개씩 조합 만들어서 순회
    tmp = [line[:] for line in arr]                                  # 모든 경우의 수 다 해봐야 하므로 arr 복사
    total = 0

    for x, y in com:                                                 # 벽 세우기
        tmp[x][y] = 1

    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 2:                                        # 바이러스면
                bfs(i, j)                                             # 퍼트리기

    for i in tmp:                                                     # tmp 행 돌면서
        total += i.count(0)                                           # 안전지역 카운트

    result = max(result, total)                                       # max 값 갱신

print(result)