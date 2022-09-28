import sys
input = lambda: sys.stdin.readline()
from collections import deque


deltas = [
    (0, 1),   # 상
    (1, 0),   # 좌
    (0, -1),  # 하
    (-1, 0),  # 우
]
result = 0  #결과값

# 1.입력받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
shark = None  # 상어 위치
weight = 2
eat_count = 0 # 음식 count
for y in range(N):
    for x in range(N):
        if arr[y][x] == 9:
            shark = [x, y]  #상어 위치 및 크기
            arr[y][x] = 0

while True:
    # 2. 가까운 거리를 찾기 위해서 bfs delta탐색
    move = deque()
    target = []  # 먹을 수 있는 고기들
    visited = [[0 for _ in range(N)]for _ in range(N)]
    move.append((shark[0], shark[1], 0))
    while move:    
        x, y, pre_vi = move.popleft()          # 데큐로 이동중인 상어 위치, 방문거리
        if target and target[0][2] == pre_vi:  # 데큐를 한번만 순회시키기 위해서, 타겟을 찾은 다음, visited값이 같으면 멈춘다.
            break  
        for delta in deltas:  #델타 탐색
            go_x = x + delta[0]
            go_y = y + delta[1]
            if 0 <= go_x < N and 0 <= go_y < N and arr[go_y][go_x] <= weight and visited[go_y][go_x] == 0:  # 사각형 안에 & 무게가 작으면 & 방문했으면
                visited[go_y][go_x] = visited[y][x] + 1
                move.append((go_x, go_y, visited[go_y][go_x]))
                if 0 < arr[go_y][go_x] < weight:                      # 무게 작은애들 다 
                    target.append((go_x, go_y, visited[go_y][go_x]))  # 타겟에 넣어버리기

    # 3. 타겟이 존재하면 움직인다.
    if target:
        target.sort(key=lambda x:(x[1],x[0]))  # 타겟 정렬
        shark[0], shark[1] = target[0][0], target[0][1]  # 타겟 처음을 먹어버림
        arr[target[0][1]][target[0][0]] = 0              # 먹어서 없어짐
        eat_count += 1                                   # 먹은 count += 1
        if eat_count == shark[2]:                        # 레벨업 조건
            shark[2] += 1
            eat_count = 0
        result += target[0][2]  # 거리만큼 더한다.
    # 4. 타겟이 존재하지 않으면 터진다.
    else:
        print(result)
        exit()

# 골드3 / 90분 / 100ms

