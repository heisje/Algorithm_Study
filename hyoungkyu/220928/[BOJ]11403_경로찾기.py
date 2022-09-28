# 실버1 / 340ms 
import sys
input = lambda:sys.stdin.readline().strip()

def DFS(i, j):                      # DFS 외우자..
    stack = [0] * N
    check = [0] * N
    top = -1
    check[i] = 1
    while True:
        for w in arr[i]:
            if w == j:              # i -> j 경로가 있으니까 1
                return 1

            if check[w] == 0:
                top += 1
                stack[top] = i
                i = w
                check[i] = 1
                break
        else:
            if top != -1:
                i = stack[top]
                top -= 1
            else:                   # i -> j 경로가 없으므로 0
                return 0

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
arr = [[] for _ in range(N)]
answer = [[0] * N for _ in range(N)]
for i in range(N):                  # 경로 만들기
    for j in range(N):
        if lst[i][j] == 1:
            arr[i].append(j)

for i in range(N):                  # 경로 확인 후 배열에 입력
    for j in range(N):
        answer[i][j] = DFS(i, j)

for i in answer:                    # 출력
    print(*i)