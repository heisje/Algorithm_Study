def clean(_i, _j):  # 제자리 청소
    matrix[_i][_j] = 2  # 청소한 곳은 2로 만든다
    return


def search(_i, _j, dr):
    global pos_i
    global pos_j
    global direction
    for k in range(1, 5):
        if matrix[_i + di[dr - k]][_j + dj[dr - k]] == 0:
            break
    else:
        return False  # 청소할 곳이 없으면 False 리턴
    if dr - k < 0:
        new_dr = dr - k + 4
    else:
        new_dr = dr - k
    pos_i, pos_j, direction = _i + di[dr - k], _j + dj[dr - k], new_dr  # 청소할 곳으로 이동 및 방향 갱신
    return True


def move_back(_i, _j, dr):
    global pos_i
    global pos_j

    new_pos_i, new_pos_j = _i + di[dr - 2], _j + dj[dr - 2]
    if matrix[new_pos_i][new_pos_j] == 1:
        return False
    else:
        pos_i = new_pos_i
        pos_j = new_pos_j
        return True


# 0: 북, 1: 동, 2:남, 3:서
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

matrix = []
N, M = map(int, input().split())
pos_i, pos_j, direction = map(int, input().split())
for i in range(N):
    matrix.append(list(map(int, input().split())))

cnt = 1
clean(pos_i, pos_j)
while (True):
    if search(pos_i, pos_j, direction):  # 청소할 곳을 찾은 경우
        clean(pos_i, pos_j)
        cnt += 1

    else:  # 찾지못하면 후진
        if move_back(pos_i, pos_j, direction):
            continue  # 후진 후 다시 서치
        else:
            break  # 후진 불가시 끝
print(cnt)