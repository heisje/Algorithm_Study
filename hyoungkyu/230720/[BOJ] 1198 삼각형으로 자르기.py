# 실버2 / 52ms
import sys
input = sys.stdin.readline

N = int(input())
dots = [list(map(int, input().split())) for _ in range(N)]
i = 0

# 넓이 구하는 공식
def func(lst):
    lst += [lst[0]]
    tmp = 0
    for i in range(3):
        tmp += lst[i][0]*lst[i+1][1] - lst[i+1][0]*lst[i][1]
    return abs(tmp)/2

maxV = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            lst = [dots[i], dots[j], dots[k]]
            tmp = func(lst)
            maxV = max(maxV, tmp)
print(maxV)
