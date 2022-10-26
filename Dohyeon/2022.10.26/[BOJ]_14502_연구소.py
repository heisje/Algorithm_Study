import copy

def spread(x, y):                       # BFS 로 바이러스가 퍼지는 함수
    q = [(x, y)]
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    while(q):
        node = q.pop(0)
        for i in range(4):
            new_i = node[0] + di[i]
            new_j = node[1] + dj[i]

            if new_matrix[new_i][new_j] == 0:
                new_matrix[new_i][new_j] = 2
                q.append((new_i, new_j))

            else:
                continue


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
N, M = map(int, input().split())                # 주어진 매트릭스 주변에 1로 벽을 쳐둔다.
matrix = [[1 for i in range(M + 2)]]
for i in range(N):
    tmp = [1] + list(map(int, input().split())) + [1]
    matrix.append(tmp)
matrix.append([1 for i in range(M + 2)])

max_cnt = 0

for num1 in range(M + 1, (N + 2)*(M + 2) - M - 2):  # 첫번째 벽
    i_1 = num1 // (M + 2)
    j_1 = num1 % (M + 2)
    if matrix[i_1][j_1] != 0:
        continue
    for num2 in range(num1 + 1, (N + 2)*(M + 2) - M - 1):   # 두번째 벽
        i_2 = num2 // (M + 2)
        j_2 = num2 % (M + 2)
        if matrix[i_2][j_2] != 0:
            continue
        for num3 in range(num2 + 1, (N + 2)*(M + 2) - M):   # 세번째 벽
            i_3 = num3 // (M + 2)
            j_3 = num3 % (M + 2)
            if matrix[i_3][j_3] != 0:
                continue
            else:                       # 세 개의 벽이 모두 생성될 때
                matrix[i_1][j_1] = 1
                matrix[i_2][j_2] = 1
                matrix[i_3][j_3] = 1

                cnt = 0
                new_matrix = copy.deepcopy(matrix)
                for i in range(N + 2):
                    for j in range(M + 2):
                        if matrix[i][j] == 2:       # 바이러스 위치를 찾는다.
                            for k in range(4):
                                if matrix[i + di[k]][j + dj[k]] == 0:   # 퍼질수 있는지 확인
                                    break
                            else:
                                continue
                            spread(i, j)

                for i_ in range(1, N + 1):
                    for j_ in range(1, M + 1):
                        if new_matrix[i_][j_] == 0:
                            cnt += 1

                if cnt > max_cnt:
                    for i_ in range(N + 2):
                        max_cnt = cnt

                matrix[i_1][j_1] = 0
                matrix[i_2][j_2] = 0
                matrix[i_3][j_3] = 0

print(max_cnt)