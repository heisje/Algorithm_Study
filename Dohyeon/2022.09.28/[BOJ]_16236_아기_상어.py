import sys
input = lambda: sys.stdin.readline().strip()
N = int(input())

matrix = [[100 for i in range(N + 2)]]   # 100짜리 물고기로 주위에 벽을 쳐줄 것이다.
fish = []
shark_level = 2
shark_exp = 0

shark_x = 0                                     # 그냥 의미없는 초기값, 후에 값을 넣을것
shark_y = 0

for i in range(N):
    line = list(map(int, input().split()))      # matrix안에 집어넘는김에 물고기 크기들이랑 상어 위치 확인
    for j in range(len(line)):
        if line[j] != 0:
            if line[j] == 9:
                shark_x = i + 1                 # 벽 때문에 +1 씩 해줘야 인덱스가 맞음
                shark_y = j + 1
                continue
            fish.append(line[j])
    line = [100] + line + [100]
    matrix.append(line)
matrix.append([100 for i in range(N + 2)])       # 10으로 된 벽을 쳐줄 것이다.
fish.sort()

time = 0

matrix[shark_x][shark_y] = 0

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
# 여기서부터 좌표값은 행값 *100 + 열값으로 암호처럼 만든다. 방문확인을 쉽게하기위해
while(fish and fish[0] < shark_level):          # 물고기가 존재하면서 먹을수 있는 물고기일경우만 가능
    queue = [shark_x * 100 + shark_y]
    visited = {shark_x * 100 + shark_y : 0}
    done = False

    found_fish = []                             # 찾아낸 최소거리 물고기들의 리스트
    min_dist = (N + 1)*(N + 1)

    while(queue):
        node = queue.pop(0)

        temp_i = node // 100
        temp_j = node % 100
        if visited[node] == min_dist:           # pop해서 뽑아낸 것이 최소거리이면 이미 최소거리 내에 물고기는 다 확인했다는 뜻
            done = True                         # 그러니 빠져나온다.
            break
        for i in range(4):
            new_pos_x = temp_i + dx[i]
            new_pos_y = temp_j + dy[i]

            try:
                okay = visited[new_pos_x * 100 + new_pos_y]     # 키에러로 방문을 확인하자
                continue
            except KeyError:
                if matrix[new_pos_x][new_pos_y] > shark_level:      # 큰 물고기로는 못지나감
                    continue
                elif matrix[new_pos_x][new_pos_y] == shark_level or matrix[new_pos_x][new_pos_y] == 0:   # 같은 물고기 크기면 지나만 갈 수 있다...
                    queue.append(new_pos_x * 100 + new_pos_y)
                    visited[new_pos_x * 100 + new_pos_y] = visited[node] + 1

                else:
                    queue.append(new_pos_x * 100 + new_pos_y)
                    visited[new_pos_x * 100 + new_pos_y] = visited[node] + 1

                    found_fish.append(new_pos_x*100 + new_pos_y)                    # 찾아낸 먹을 수 있는 물고기 리스트에 저장
                    min_dist = visited[node] + 1                                    # 가장 먼저 찾아내었을 때가 최소 거리
    if found_fish:
        target = min(found_fish)                # 가장 작은 값이 가장 위이며 왼쪽인 값이 된다.
        time += visited[target]                 # 거리만큼 걸린 시간을 더해준다.
        shark_x, shark_y = target // 100 , target % 100     # 좌표 암호 해독
        fish.remove(matrix[shark_x][shark_y])               # 해당 위치 값을 남은 물고기 리스트에서 제거
        matrix[shark_x][shark_y] = 0                        # 해당 위치를 비워줌
        shark_exp += 1

    if shark_exp == shark_level:            # 상어 레벨업 확인
        shark_exp = 0
        shark_level += 1
    if not done:                            # bfs를 돌려는데 먹을게 없을 경우
        break

print(time)

