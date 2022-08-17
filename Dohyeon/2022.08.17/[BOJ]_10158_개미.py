import sys
input = lambda: sys.stdin.readline().strip()

w, h = map(int, input().split())
pos_x, pos_y = map(int, input().split())

t = int(input())

direction = 1                               # 오른쪽 위 : 1, 왼쪽 위 : 2, 왼쪽 아래 : 3, 오른쪽 아래 : 4

for move in range(t):

    if direction == 1:
        pos_x += 1
        pos_y += 1
        if pos_x == w and pos_y == h:
            direction = 3                   # 꼭지점에 부딪히면 반대로 돌아간다
        elif pos_x == w:
            direction = 2                   # 오른쪽 변에 닿을 경우 왼쪽 위로
        elif pos_y == h:
            direction = 4                   # 천장에 닿을 경우 오른쪽 아래로


    elif direction == 2:
        pos_x -= 1
        pos_y += 1
        if pos_x == 0 and pos_y == h:       # 꼭지점에 부딪히면 반대로 돌아간다
            direction = 4
        elif pos_x == 0:                    # 왼쪽 변에 닿을 경우 오른쪽 위로
            direction = 1
        elif pos_y == h:                    # 천장에 닿을 경우 왼쪽 아래로
            direction = 3


    elif direction == 3:
        pos_x -= 1
        pos_y -= 1
        if pos_x == 0 and pos_y == 0:       # 꼭지점에 부딪히면 반대로 돌아간다
            direction = 1
        elif pos_x == 0:                    # 왼쪽 변에 닿을 경우 오른쪽 아래로
            direction = 4
        elif pos_y == 0:                    # 바닥에 닿을 경우 왼쪽 위로
            direction = 2

    else:                                   # 오른쪽 아래 방향의 경우
        pos_x += 1
        pos_y -= 1
        if pos_x == w and pos_y == 0:       # 꼭지점에 부딪히면 반대로 돌아간다
            direction = 2
        elif pos_x == w:                    # 오른쪽 변에 닿으면 왼쪽 아래로
            direction = 3
        elif pos_y == 0:                    # 바닥에 닿으면 오른쪽 위로
            direction = 1
print(pos_x, end=' ')
print(pos_y)


