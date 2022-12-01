
from collections import deque

N = int(input())
N_list = list(range(N))
color_board = []
for i in range(N):
    color_board.append(list(str(input())))

print(color_board)

checking_board = [[0 for i in range(N)] for j in range(N)]

route_list = {}
for i in range(N):
    for j in range(N):

        key_num = i * 1000 + j
        route_list[key_num] = []
        temp1 = [i - 1, i, i + 1]
        temp2 = [j - 1, j, j + 1]

        for a1 in temp1:
            if a1 not in N_list:
                continue
            route_list[key_num].append(a1*1000 + j)

        for a2 in temp2:
            if a2 not in N_list:
                continue
            route_list[key_num].append(i*1000 + a2)

        temp_set = set(route_list[key_num])  # 중복제거
        route_list[key_num] = list(temp_set)

def BFS_Color(N):

    counting_num = 1


