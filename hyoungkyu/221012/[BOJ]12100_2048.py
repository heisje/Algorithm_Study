# 골드2 / 820ms
from copy import deepcopy
import sys
input = lambda:sys.stdin.readline().strip()

def up(arr):
    global maxV
    for i in range(N):
        for j in range(N-1):
            for k in range(j+1, N):                                 # 첫번째 옮길 값 찾기
                if arr[k][i] != 0:                                  # 첫번째 옮길 값 찾음
                    if arr[j][i] == 0 or arr[k][i] == arr[j][i]:    # 합쳐야 할 조건
                        if arr[j][i] == 0:                          # 만약 현재 위치의 값이 0이면
                            for l in range(k+1, N):                 # 두번째 옮길 값 찾아보기
                                if arr[l][i] != 0:                  # 두번재 값을 찾았을 때
                                    if arr[l][i] == arr[k][i]:      # 첫번째 옮길 값과 같으면
                                        arr[j][i] += arr[l][i]      # 두번째 옮길 값을 현재 위치에 더하기
                                        arr[l][i] = 0               # 합쳐진 값 위치를 0으로 초기화
                                    break
                        arr[j][i] += arr[k][i]                      # 첫번째 옮길 값을 현재 위치에 더하기
                        arr[k][i] = 0                               # 합쳐진 값 위치를 0으로 초기화
                    break
            if maxV < arr[j][i]:                                    # 합쳐진 값이 최대값이면 갱신
                maxV = arr[j][i]

def down(arr):
    global maxV
    for i in range(N):
        for j in range(N-1, 0, -1):
            for k in range(j-1, -1, -1):
                if arr[k][i] != 0:
                    if arr[j][i] == 0 or arr[k][i] == arr[j][i]:
                        if arr[j][i] == 0:
                            for l in range(k-1, -1, -1):
                                if arr[l][i] != 0:
                                    if arr[l][i] == arr[k][i]:
                                        arr[j][i] += arr[l][i]
                                        arr[l][i] = 0
                                    break
                        arr[j][i] += arr[k][i]
                        arr[k][i] = 0
                    break
            if maxV < arr[j][i]:
                maxV = arr[j][i]

def left(arr):
    global maxV
    for i in range(N):
        for j in range(N-1):
            for k in range(j+1, N):
                if arr[i][k] != 0:
                    if arr[i][j] == 0 or arr[i][k] == arr[i][j]:
                        if arr[i][j] == 0:
                            for l in range(k+1, N):
                                if arr[i][l] != 0:
                                    if arr[i][l] == arr[i][k]:
                                        arr[i][j] += arr[i][l]
                                        arr[i][l] = 0
                                    break
                        arr[i][j] += arr[i][k]
                        arr[i][k] = 0
                    break
            if maxV < arr[i][j]:
                maxV = arr[i][j]

def right(arr):
    global maxV
    for i in range(N):
        for j in range(N-1, 0, -1):
            for k in range(j-1, -1, -1):
                if arr[i][k] != 0:
                    if arr[i][j] == 0 or arr[i][k] == arr[i][j]:
                        if arr[i][j] == 0:
                            for l in range(k-1, -1, -1):
                                if arr[i][l] != 0:
                                    if arr[i][l] == arr[i][k]:
                                        arr[i][j] += arr[i][l]
                                        arr[i][l] = 0
                                    break
                        arr[i][j] += arr[i][k]
                        arr[i][k] = 0
                    break
            if maxV < arr[i][j]:
                maxV = arr[i][j]

def f(arr, cnt):                        # 5번 이동시킬때까지 완전탐색(?)
    if cnt == 5:
        return 
    else:
        tmp_arr = deepcopy(arr)         # deepcopy 안하고 arr[:] 하니까 얕은 복사 발생해서 계산 제대로 안됨
        up(tmp_arr)
        f(tmp_arr, cnt+1)

        tmp_arr = deepcopy(arr)
        down(tmp_arr)
        f(tmp_arr, cnt+1)

        tmp_arr = deepcopy(arr)
        left(tmp_arr)
        f(tmp_arr, cnt+1)

        tmp_arr = deepcopy(arr)
        right(tmp_arr)
        f(tmp_arr, cnt+1)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0                                 # 이동 횟수
maxV = 0                                # 최대값 선언
for i in range(N):
    for j in range(N):
        if maxV < arr[i][j]:
            maxV = arr[i][j]            # 초기 최대값 설정
f(arr, cnt)
print(maxV)
