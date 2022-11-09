# 골드3 / 72ms
import sys
input = lambda:sys.stdin.readline().strip()

D = [[0, 1], [1, 0]]                                    # 우, 하

def f(i, j, direction):                                 # i, j : 현재 위치, direction : 가로 or 세로
    check = 1                                           # 경사로를 놓을 수 있는 칸 카운트
    slope = False                                       # 경사로를 놓아야 되는 상황을 나타내는 변수
    ci, cj = i, j
    for _ in range(N-1):
        ni, nj = ci+direction[0], cj+direction[1]       # 해당 줄에서 한칸씩 이동
        if arr[ci][cj] == arr[ni][nj]:                  # 다음 칸이랑 같으면 카운트 +1
            check += 1

        elif arr[ci][cj]-1 == arr[ni][nj]:              # 내리막인 경우
            if slope:                                   # 이미 경사로를 놓아야 되는 상황이면 Fail
                return 0
            slope = True                                # 내리막인 경우 다음 칸들에 경사로를 놓아야 되므로 경사로 체크
            check = 1                                   # 경사로를 놓을 수 있는지 카운트를 다시 셈

        elif arr[ci][cj]+1 == arr[ni][nj]:              # 오르막인 경우
            if check < L:                               # 이전에 경사로를 놓아야 되지만 그럴 칸이 없는 경우 Fail
                return 0
            else:                                       # 이전에 경사로를 놓을 수 있으면 해당 칸부터 다시 계속 진행
                check = 1
        else:                                           # 규칙에 어긋난 경우 Fail
            return 0

        if slope and check >= L:                        # 내리막을 설치할 수 있는 경우
            slope = False
            check = 0

        ci, cj = ni, nj
    if slope:                                           # 범위를 벗어난 경사로가 있으면 Fail
        return 0
    # print(i, j)
    return 1                                            # 길을 찾은 경우

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
for k in range(N):
    cnt += f(0, k, D[1]) + f(k, 0, D[0])
print(cnt)