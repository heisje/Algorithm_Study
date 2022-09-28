import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 처음 위치 찾기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            si, sj = i, j
            arr[i][j] = 0
            break
    else:
        continue
    break

size = 2            # 아기 상어 크기
time = 0            # 잡아먹는데 걸린 시간
eaten = 0           # 사이즈 늘리기 위해 얼마나 먹었는지 체크
answer = 0          # 결과값 갱신을 위한 변수

while True:
    q = deque()
    q.append((time, si, sj))
    visited = [[0] * N for _ in range(N)]
    candidates = []                                 # 먹을 수 있는 물고기 후보군
    limit = 999999
    while q:
        time, ci, cj = q.popleft()
        if limit < time:                            # 가지치기
            break
        if arr[ci][cj] != 0 and arr[ci][cj] < size: # 빈 칸이 아니고 size 보다 작다면 먹을 수 있는 후보군에 올린다
            candidates.append((ci, cj, time))       # 나중에 i, j 기준으로 정렬할거라 이 순서로 넣어주기
            limit = time                            # 초별로 끊어서 보기 위해서

        # 지나갈 수 있는 곳 찾기
        for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] <= size:
                visited[ni][nj] = 1
                q.append((time+1, ni, nj))


    candidates.sort()                       # 가장 위에 있는 물고기, 가장 왼쪽에 있는 물고기 조건 순으로 정렬
    if candidates:                          # 먹을 물고기가 있다면
        si, sj, time = candidates[0]        # 그거 먹고 다시 아기 상어 위치 설정
        answer = time                       # 현재까지 소요 시간
        arr[si][sj] = 0                     # 0으로 처리해서 먹었다고 표시
        eaten += 1                          # size 늘리기 위해 먹은 마리수 더해주기
        if eaten == size:                   # 먹은 마리수와 size 가 같다면
            size += 1                       # 사이즈 늘려주고
            eaten = 0                       # 다시 초기화
    else:                                   # 먹을 후보군이 없다면
        break                               # 종료하고 answer 반환하기

print(answer)

