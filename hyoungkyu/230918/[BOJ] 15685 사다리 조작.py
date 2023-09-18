# 골드3 / 764ms
import sys
input = sys.stdin.readline

# N: 세로선 개수, M: 가로선 개수, H: 가로선을 놓을 수 있는 위치의 개수
N, M, H = map(int, input().split())
arr = [[0]*(N+1) for _ in range(H+1)]
for _ in range(M):
    a, b = map(int ,input().split())
    arr[a][b] = b+1
    arr[a][b+1] = b

answer = 4

def solution(i, j, cnt):
    global answer
    if is_possible():
        answer = min(answer, cnt)
        return
    
    if cnt >= 3 or answer <= cnt: return

    for ni in range(i, H+1):
        for nj in range(1, N):
            if ni == i and nj < j: continue
            if not arr[ni][nj] and not arr[ni][nj+1]:
                arr[ni][nj] = nj+1
                arr[ni][nj+1] = nj
                solution(ni, nj, cnt+1)
                arr[ni][nj] = 0
                arr[ni][nj+1] = 0
    
    return

def is_possible():
    for j in range(1, N+1):
        ci=1
        cj=j
        while ci<H+1:
            if arr[ci][cj]:
                cj = arr[ci][cj]
                ci += 1
            else:
                ci += 1
        if cj != j:
            return False
    return True
    
solution(1, 1, 0)
print(answer if answer != 4 else -1)

# for i in range(1, H+1):
#     print(arr[i][1:])
