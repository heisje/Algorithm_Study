from collections import deque
n, m = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))


time = 0
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
count_cheese = 0
while(True):
    last_cheese = count_cheese
    count_cheese = 0
    check = False
    que = deque()
    que.append([0, 0])
    while(que):
        ele = que.popleft()

        if matrix[ele[0]][ele[1]] == 1:
            matrix[ele[0]][ele[1]] = time + 2
            count_cheese += 1
            check = True
            continue
        elif matrix[ele[0]][ele[1]] == time + 2:
            continue
        elif matrix[ele[0]][ele[1]] == -(time + 2):
            continue
        else:
            matrix[ele[0]][ele[1]] = -(time + 2)

        for i in range(4):
            new_x = ele[0] + di[i]
            new_y = ele[1] + dj[i]
            if new_x < 0 or new_x == n:
                continue
            if new_y < 0 or new_y == m:
                continue

            que.append([new_x, new_y])
    time += 1
    if check == False:
        break
print(time - 1)
print(last_cheese)