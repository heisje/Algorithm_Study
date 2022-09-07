# 76ms
import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()
# lst = [[2, 4], [4, 6], [5, 3], [8, 10], [11, 4], [13, 6], [15, 8]]
tot = 0                   
maxV = 0                                                                                        
stack = [0]*(lst[-1][0]+1)
for i in range(N):
    if maxV < lst[i][1]:
        maxV = lst[i][1]
        idx = lst[i][0]

for i in range(N):
    stack[lst[i][0]] = lst[i][1]
    # stack = [0, 0, 4, 0, 6, 3, 0, 0, 10, 0, 0, 4, 0, 6, 0, 8]

# 왼쪽부터 직사각형 더하기
tmp = 0
for i in range(idx+1):  # +1 : 젤 높은 부분의 넓이도 구하려고
    if stack[i] > tmp:
        tmp = stack[i]
    tot += tmp

# 오른쪽부터 직사각형 더하기
tmp = 0 
for i in range(lst[-1][0], idx, -1):
    if stack[i] > tmp:
        tmp = stack[i]
    tot += tmp
print(tot)