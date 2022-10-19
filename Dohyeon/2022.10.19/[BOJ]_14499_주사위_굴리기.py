N, M, x, y, K = map(int, input().split())
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

orders = list(map(int, input().split()))


"""
해결아이디어
        1
    2   3   4
        5
        6
각 번호는 면을 의미, 1~4로 굴릴 때 변하는 것을 확인하자
3번면이 항상 밑이라고 생각하자
6번면을 출력한다.
"""
face1 = 0
face2 = 0
face3 = 0
face4 = 0
face5 = 0
face6 = 0

if matrix[x][y] != 0:
    face3 = matrix[x][y]

dx = [0, 0, 0, -1, 1]       # 0번인덱스는 안씀, 편의를 위해 존재
dy = [0, 1, -1, 0, 0]

for order in orders:


    new_x = x + dx[order]
    new_y = y + dy[order]
    if new_x < 0 or new_x == N or new_y < 0 or new_y == M:
        continue

    if order == 1:
        face2, face3, face4, face6 = face3, face4, face6, face2
    elif order == 2:
        face2, face3, face4, face6 = face6, face2, face3, face4
    elif order == 3:
        face1, face3, face5, face6 = face6, face1, face3, face5
    else:
        face1, face3, face5, face6 = face3, face5, face6, face1

    if matrix[new_x][new_y] == 0:
        matrix[new_x][new_y] = face3
    else:
        face3 = matrix[new_x][new_y]
        matrix[new_x][new_y] = 0
    x = new_x
    y = new_y

    print(face6)

