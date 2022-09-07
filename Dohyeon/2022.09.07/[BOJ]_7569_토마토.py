
import sys
input = sys.stdin.readline
M, N, H = map(int, input().split())

# 거리 탐색으로 풀어보자

tomato = [[[0 for i in range(M)] for j in range(N)] for k in range(H)]
tomato2 = [[[0 for i in range(M)] for j in range(N)] for k in range(H)]
visited = {}

H_list = list(range(H))
N_list = list(range(N))
M_list = list(range(M))

for k in range(H):
    for j in range(N):
        temp_list = list(map(int, input().split()))
        for i in range(M):
            tomato[k][j][i] = temp_list[i]
            key_num = k*1000000 + j*1000 + i
            visited[key_num] = []
            temp1 = [k-1, k, k+1]
            temp2 = [j-1, j, j+1]
            temp3 = [i-1, i, i+1]

            for a1 in temp1:
                if a1 not in H_list:
                    continue
                visited[key_num].append(a1 * 1000000 + j * 1000 + i)
            for a2 in temp2:
                if a2 not in N_list:
                    continue
                visited[key_num].append(k * 1000000 + a2 * 1000 + i)
            for a3 in temp3:
                if a3 not in M_list:
                    continue
                visited[key_num].append(k * 1000000 + j * 1000 + a3)
            temp_set = set(visited[key_num])                            # 중복제거
            visited[key_num] = list(temp_set)


#print(visited)


def BFS_tomato(m, n, h):
    max_count = -1
    global visited
    global tomato
    global tomato2
    for k in range(h):
        for j in range(n):
            for i in range(m):

                day = 0
                check_all = True
                if tomato[k][j][i] == 1:
                    que = [k*1000000 + j*1000 + i]
                    tomato_map = tomato[:]
                    for_depth_map = tomato2[:]
                    while que:
                        v = que.pop(0)
                        for w in visited[v]:
                            if tomato_map[w//1000000][(w//1000)%1000][w%1000] == -1:
                                continue
                            elif tomato_map[w//1000000][(w//1000)%1000][w%1000] == 1:
                                continue
                            else:
                                tomato_map[w//1000000][(w//1000)%1000][w%1000] = 1
                                for_depth_map[w//1000000][(w//1000)%1000][w%1000] = for_depth_map[v//1000000][(v//1000)%1000][v%1000] + 1
                                que = que + visited[w]

                else:
                    continue

                for k in range(h):
                    for j in range(n):
                        for i in range(m):
                            if for_depth_map[k][j][i] > day:
                                day = for_depth_map[k][j][i]
                            if tomato_map[k][j][i] == 0:
                                check_all = False

                if check_all == False:
                    continue

                else:
                    if max_count < day:
                        max_count = day


    return max_count



result = BFS_tomato(M, N, H)
print(result)