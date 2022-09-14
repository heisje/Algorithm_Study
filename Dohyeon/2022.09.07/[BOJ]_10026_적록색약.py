
N = int(input())
arr = []
N_list = list(range(N))

for n in range(N):
    arr.append(list(input()))
checking_board = [[0 for i in range(N)] for j in range(N)]
checking_board2 = [[0 for i in range(N)] for j in range(N)]
counting_num = 0
for i in range(N):
    for j in range(N):
        if checking_board[i][j] == 0:
            counting_num += 1
            if arr[i][j] == "R":
                check_color = "R"
            elif arr[i][j] == "B":
                check_color = "B"
            else:
                check_color = "G"
            queue = [(i, j)]
            while queue:
                x, y = queue.pop(0)

                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if (x + dx) not in N_list or (y + dy) not in N_list:
                        continue
                    if arr[x + dx][y + dy] == check_color and checking_board[x + dx][y + dy] == 0:
                        checking_board[x + dx][y + dy] = counting_num
                        queue.append((x + dx, y + dy))

counting_num2 = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == "G":
            arr[i][j] = "R"
for i in range(N):
    for j in range(N):
        if checking_board2[i][j] == 0:
            counting_num2 += 1
            if arr[i][j] == "B":
                check_color = "B"
            else:
                check_color = "R"
            queue = [(i, j)]
            while queue:
                x, y = queue.pop(0)
                #if x not in N_list or y not in N_list:
                #    continue

                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if (x + dx) not in N_list or (y + dy) not in N_list:
                        continue
                    if arr[x +dx][y + dy] == check_color and checking_board2[x + dx][y + dy] == 0:
                        checking_board2[x + dx][y + dy] = counting_num2
                        queue.append((x + dx, y + dy))


print(counting_num, counting_num2)
