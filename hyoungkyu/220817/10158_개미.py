# 72ms

import sys
input = lambda: sys.stdin.readline().strip()

w, h = map(int, input().split())            # h x w 행렬
p, q = map(int, input().split())            # 현재 위치 입력
t = int(input())                            # 시간 t 입력

t_x = t % (2 * w)                           # x좌표는 2*w의 주기를 가짐
t_y = t % (2 * h)                           # y좌표는 2*h의 주기를 가짐

# X 좌표 구하기
if t_x > w - p:                             # 처음 위치에서 오른쪽으로 이동하여 반사된다면
    t_x = t_x - (w - p)                     # 오른쪽 칸 만큼 빼주고 위치를 오른쪽에 고정

    if t_x > w:                             # 남은 이동횟수가 w보다 커서 반사된다면
        t_x = t_x - w                       # 위치를 왼쪽벽으로 고정
        X = t_x                             # 남은 이동횟수로 최종 X좌표 구하기

    else:                                   # 오른쪽에서 반사되고 남은 횟수만큼 이동하여 최종 X좌표 구하기
        X = w - t_x                         

else:                                       # 처음 위치에서 오른쪽 공간 내에서 움직인다면
    X = p + t_x

# Y 좌표 구하기
if t_y > h - q:
    t_y = t_y - (h - q)
    if t_y > h:
        t_y = t_y - h
        Y = t_y
    else:
        Y = h - t_y
else:
    Y = q + t_y

print(X, Y)

