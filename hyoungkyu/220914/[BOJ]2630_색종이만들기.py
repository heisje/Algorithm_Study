# 실버2 / 84ms
import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
dic = {0 : 0, 1 : 0}
def fn(x, y, N):
    if N == 1:
        dic[lst[x][y]] += 1
        return
    flag = False
    for i in range(N):
        for j in range(N):
            if lst[x+i][y+j] != lst[x][y]:
                flag = True
                break
        if flag:
            break
    else:
        dic[lst[x][y]] += 1
        return
    for i in range(0, N, N//2):
        for j in range(0, N, N//2):
            fn(x+i, y+j, N//2)

fn(0, 0, N)
print(dic[0])
print(dic[1])