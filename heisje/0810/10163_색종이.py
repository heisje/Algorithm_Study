#실패
import sys

#최대 1001칸까지므로 0~1000 까지 만듬
N = int(input())

counter = [0 for _ in range(N)] #0을 N만큼 제작
x1 = [0 for _ in range(N)]
y1 = [0 for _ in range(N)]
x2 = [0 for _ in range(N)]
y2 = [0 for _ in range(N)]
for i in range(N):  #사각형마다 i값을 넣어줘서 구분지음
    X, Y, W, H = map(int, sys.stdin.readline().split())
    x1[i] = X
    y1[i] = Y
    x2[i] = X + W
    y2[i] = Y + H
x_min = min(x1)
y_min = min(y1)

for i in range(N):
    x1[i] -= x_min
    x2[i] -= x_min
    y1[i] -= y_min
    y2[i] -= y_min

li = [[None for _ in range(max(x2) + 1)] for _ in range(max(y2) + 1)]
for i in range(N):
    for y in range(y1[i], y2[i]):
        for x in range(x1[i], x2[i]):
            li_y_x = li[y][x] #li를 너무 많이 참조해서 틀리나 싶어서 이케해봄
            if li_y_x != i:              #사각형 안씌운 칸이면
                if li_y_x != None:       #
                    counter[li_y_x] -= 1
                counter[i] += 1
                li[y][x] = i 
    
for num in counter:
    print(num)