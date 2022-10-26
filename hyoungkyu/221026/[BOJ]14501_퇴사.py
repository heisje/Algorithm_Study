# 실버3 / 88ms
import sys
input = lambda:sys.stdin.readline().strip()

N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

def f(i, tmp):
    global maxV
    if i < N:
        if i + lst[i][0] <= N :
            if lst[i][1] + tmp > maxV:
                maxV = lst[i][1] + tmp
            f(i+lst[i][0], tmp+lst[i][1])
        f(i+1, tmp)

maxV = 0
f(0, 0)
print(maxV)