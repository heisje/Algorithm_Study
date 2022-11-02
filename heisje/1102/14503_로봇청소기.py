# https://www.acmicpc.net/problem/14503
from collections import deque

DELTA = (
    (0, -1), # 상
    (1, 0), # 우
    (0, 1), # 하
    (-1, 0), # 좌
)


N, M = list(map(int, input().split()))
c, r, d = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
#print(arr)
clean_count = 2
while True:
    #print(clean_count,' ',r,c, ' ',d)
    # 1. 제자리 청소
    if arr[c][r] == 0:
        arr[c][r] = clean_count
        clean_count += 1

    # 청소할 방향 찾기
    for d_idx in range(1, 5):
        go_d = (d + 4 - d_idx) % 4
        go_r = r + DELTA[go_d][0]
        go_c = c + DELTA[go_d][1]
        if arr[go_c][go_r] == 0:
            r, c, d = go_r, go_c, go_d
            break
    # 후진
    else:
        r = r - DELTA[d][0]
        c = c - DELTA[d][1]
        if arr[c][r] == 1:
            # for n in range(N):
            #     print(arr[n])
            print(clean_count-2)
            exit()
    
# 골드5 / 30분