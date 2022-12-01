import copy

def DFS(matrix, n):
    global result
    cctv_direction = [
        [],
        [[0], [1], [2], [3]],
        [[0, 1], [2, 3]],
        [[0, 2], [0, 3], [1, 2], [1, 3]],
        [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
        [[0, 1, 2, 3]]
    ]
    if n == len(cctv):
        temp = 0
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 0:
                    temp += 1
        if temp < result:
            result = temp

    else:

        pos_i, pos_j, cctype = cctv[n]
        for dir in cctv_direction[cctype]:
            new_matrix = copy.deepcopy(matrix)
            check_space(new_matrix, pos_i, pos_j, dir)
            DFS(new_matrix, n + 1)




def check_space(newmatrix, pos_i, pos_j, dir):
    dir_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # 상하좌우


    for d in dir:
        new_i = pos_i
        new_j = pos_j
        while True:

            new_i += dir_list[d][0]          # 계속 한쪽 방향으로 진행해본다
            new_j += dir_list[d][1]

            if 0 <= new_i < N and 0 <= new_j < M:
                if newmatrix[new_i][new_j] == 6:
                    break
                elif newmatrix[new_i][new_j] == 0:
                    newmatrix[new_i][new_j] = "#"
            else:
                break


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
result = N*M

cctv = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] != 0 and matrix[i][j] != 6:
            cctv.append((i, j, matrix[i][j]))       # 감시카메라 위치와 종류를 저장해두자

DFS(matrix, 0)
print(result)
