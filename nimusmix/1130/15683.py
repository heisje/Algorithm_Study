import sys
from collections import defaultdict, deque
input = lambda: sys.stdin.readline().strip()

def monitor(idx, cctv):
    for case in case_of_direction[cctv[0]]:                                   # cctv가 회전할 수 있는 경우의 수 별로 순회
        check = deque()                                                       # 감시할 수 있는 구역을 담을 리스트
        for i in range(len(case)):
            di, dj = case[i]
            ni, nj = cctv[1] + di, cctv[2] + dj
  
            while 0 <= ni < N and 0 <= nj < M and office[ni][nj] != 6:
                if office[ni][nj] == 0:                                       # 빈 칸이면 감시할 수 있는 구역에 담기
                    check.append((ni, nj))
                ni, nj = ni + di, nj + dj
                
        case_of_monitor[idx].append(check)                                    # 각 cctv의 경우의 수 별 감시 리스트 모두 추가


def dfs(dep, arr):
    global max_monitoring
    
    if dep == len(case_of_monitor):                                            # dep이 cctv의 개수와 같아지면
        arr = set(arr)                                                         # arr을 set하여 중복 없애기
        max_monitoring = max(len(arr), max_monitoring)                         # max_monitoring 갱신 후 return
        return
    
    for piece in case_of_monitor[dep]:                                         # 기존 arr에 cctv 별로 하나의 경우의 수를 extend하여 dfs
        new_arr = arr[:]
        new_arr.extend(piece)
        dfs(dep+1, new_arr)


N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
case_of_monitor = defaultdict(list)
case_of_direction = [                                                          # cctv가 감시할 수 있는 direction
    0,
    [[D[0]], [D[1]], [D[2]], [D[3]]],
    [[D[0], D[2]], [D[1], D[3]]],
    [[D[0], D[3]], [D[2], D[3]], [D[2], D[1]], [D[0], D[1]]],
    [[D[0], D[1], D[2]], [D[0], D[1], D[3]], [D[0], D[2], D[3]], [D[1], D[2], D[3]]],
    [[D[0], D[1], D[2], D[3]]]
]

max_monitoring = 0
cctvs = []
not_empty = 0
for i in range(N):
    for j in range(M):
        if office[i][j] != 0 and office[i][j] != 6:                             # cctv면
            cctvs.append((office[i][j], i, j))                                  # (cctv 번호, i, j)를 cctvs에 추가
            not_empty += 1                                                      # not_empty += 1
        elif office[i][j] == 6:                                                 # 벽이면
            not_empty += 1                                                      # not_empty += 1

for idx, cctv in enumerate(cctvs):
    monitor(idx, cctv)

dfs(0, [])

print(N * M - not_empty - max_monitoring)                                       # 사각지대의 수 = 전체 - cctv 또는 벽 - 감시할 수 있는 공간