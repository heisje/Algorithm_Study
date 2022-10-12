from itertools import product
import copy
arr = ['r', 'l', 'u', 'd']
do_list = list(product(arr, repeat=5))  # 어차피 1024개밖에 안된다.

def move_left(n):
    global max_val
    moved = False
    for i in range(n):
        before = [0, 0]
        zeros = []
        for j in range(n):
            if matrix[i][j] == 0:
                zeros.append(j)

            else:
                if before[1] == matrix[i][j]:
                    matrix[i][before[0]] = before[1] * 2
                    if matrix[i][before[0]] > max_val:
                        max_val = matrix[i][before[0]]
                    matrix[i][j] = 0
                    zeros.append(j)
                    moved = True
                    before[1] = 0
                else:
                    before[1] = matrix[i][j]
                    if zeros:
                        pos = zeros.pop(0)
                        matrix[i][pos] = matrix[i][j]
                        matrix[i][j] = 0
                        zeros.append(j)
                        before[0] = pos
                        moved = True
                    else:
                        before[0] = j

    return moved

def move_right(n):
    global max_val
    moved = False
    for i in range(n):
        before = [n - 1, 0]
        zeros = []
        for j in range(n - 1, -1, -1):
            if matrix[i][j] == 0:
                zeros.append(j)

            else:
                if before[1] == matrix[i][j]:
                    matrix[i][before[0]] = before[1] * 2
                    if matrix[i][before[0]] > max_val:
                        max_val = matrix[i][before[0]]
                    matrix[i][j] = 0
                    zeros.append(j)
                    moved = True
                    before[1] = 0
                else:
                    before[1] = matrix[i][j]
                    if zeros:
                        pos = zeros.pop(0)
                        matrix[i][pos] = matrix[i][j]
                        matrix[i][j] = 0
                        zeros.append(j)
                        before[0] = pos
                        moved = True
                    else:
                        before[0] = j

    return moved

def move_up(n):
    global max_val
    moved = False
    for j in range(n):
        before = [0, 0]
        zeros = []
        for i in range(n):
            if matrix[i][j] == 0:
                zeros.append(i)

            else:
                if before[1] == matrix[i][j]:
                    matrix[before[0]][j] = before[1] * 2
                    if matrix[before[0]][j] > max_val:
                        max_val = matrix[before[0]][j]
                    matrix[i][j] = 0
                    zeros.append(i)
                    moved = True
                    before[1] = 0
                else:
                    before[1] = matrix[i][j]
                    if zeros:
                        pos = zeros.pop(0)
                        matrix[pos][j] = matrix[i][j]
                        matrix[i][j] = 0
                        zeros.append(i)
                        before[0] = pos
                        moved = True
                    else:
                        before[0] = i

    return moved

def move_down(n):
    global max_val
    moved = False
    for j in range(n):
        before = [n - 1 , 0]
        zeros = []
        for i in range(n - 1, -1, -1):
            if matrix[i][j] == 0:
                zeros.append(i)

            else:
                if before[1] == matrix[i][j]:
                    matrix[before[0]][j] = before[1] * 2
                    if matrix[before[0]][j] > max_val:
                        max_val = matrix[before[0]][j]
                    matrix[i][j] = 0
                    zeros.append(i)
                    moved = True
                    before[1] = 0
                else:
                    before[1] = matrix[i][j]
                    if zeros:
                        pos = zeros.pop(0)
                        matrix[pos][j] = matrix[i][j]
                        matrix[i][j] = 0
                        zeros.append(i)
                        before[0] = pos
                        moved = True
                    else:
                        before[0] = i

    return moved

N = int(input())
max_val = 0

matrix_original = []

for i in range(N):
    tmp = list(map(int, input().split()))
    if max(tmp) > max_val:
        max_val = max(tmp)
    matrix_original.append(tmp)


for to_do in do_list:
    matrix = copy.deepcopy(matrix_original)
    for k in list(to_do):
        if k == 'r':
            result = move_right(N)
            if not result:
                break
        elif k == 'l':
            result = move_left(N)
            if not result:
                break
        elif k == 'u':
            result = move_up(N)
            if not result:
                break
        elif k == 'd':
            result = move_down(N)
            if not result:
                break

print(max_val)

