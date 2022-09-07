# 골드5 / 4148ms
import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

# M : 가로 칸 수, N : 세로 칸 수, H : 층 수
# 층을 딕서너리로, 배열을 리스트로 구현
M, N, H = map(int, input().split())
dic_lst = {}        # 입력 딕셔너리
dic_point = {}      # 처음에 익은 토마토의 위치를 받을 딕셔너리
dic_visited = {}    # 방문 딕셔너리
queue = deque()
# 입력 중 0의 개수를 셀 변수 -> 처음부터 다 익어있는지 확인하기 위해, 안 익은 토마토가 있는지 확인하기 위해
num = 0             
cnt = 1
for i in range(1, H+1):
    dic_lst[i] = deque(deque(map(int, input().split())) for _ in range(N))
    dic_visited[i] = deque([0]*M for _ in range(N))
    dic_point[i] = deque()
    for j in range(N):
        for k in range(M):
            if dic_lst[i][j][k] == 1:           # 처음에 익은 토마토 위치 확인
                dic_point[i].append([j, k])
                queue.append([j, k, i])
            elif dic_lst[i][j][k] == 0:         # 안 익은 토마토 개수 확인
                num += 1
            else:                               # 토마토가 없는 칸 체크
                dic_visited[i][j][k] = -1

def DFS(dic_lst, queue):
    global num
    global cnt
    D = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]] # 북,남,동,서,상,하
    if num == 0:                                # 처음 안 익은 토마토의 개수가 0이면 0 반환
        return 0
    tmp = deque()                               # 한 큐를 다 돌고나서 큐를 갱신시키기 위해 필요
    while queue:
        ni, nj, nk = queue.popleft()
        for di, dj, dk in D:
            if 0<=ni+di<N and 0<=nj+dj<M and 1<=nk+dk<=H and dic_lst[nk+dk][ni+di][nj+dj] == 0 and dic_visited[nk+dk][ni+di][nj+dj] == 0:
                tmp.append([ni+di, nj+dj, nk+dk])
                dic_visited[nk+dk][ni+di][nj+dj] = cnt
                num -= 1                        # 안 익은 토마토가 익었으므로 -1을 해준다
        if queue == deque() and tmp != deque(): # 한 큐를 다 돌면
            queue = tmp                         # 큐를 갱신
            cnt += 1                            # 시간 증가
            tmp = deque()                       # 다음 큐를 받기 위해 초기화

    if num != 0:                                # 다 돌고 나서 안 익은 토마토가 있으면 -1 반환
        return -1
    else:                                       # 마지막 부분으로 이동해서 경로가 없는걸 확인하고 끝나므로 1을 빼줘야됨
        return cnt-1
print(DFS(dic_lst, queue))


# for i in range(1, H+1):
#     for j in dic_visited[i]:
#         print(*j)

# EX)
# 5 3 2
# 0 0 0 0 0     4 3 2 3 4
# 0 0 0 0 0     3 2 1 2 3
# 0 0 0 0 0     4 3 2 3 4
# 0 0 0 0 0     3 2 1 2 3
# 0 0 1 0 0     2 1 0 1 2
# 0 0 0 0 0     3 2 1 2 3