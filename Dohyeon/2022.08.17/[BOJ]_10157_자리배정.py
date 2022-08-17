import sys

input = sys.stdin.readline

X, Y = map(int, input().split())

person = int(input())

if person > X * Y:
    print(0)

else:
    pos_x = 1
    pos_y = 1
    person_num = 1                      # 몇 번째 사람인지 확인, 사실상 대기 순서

    len_X = X
    len_Y = Y
    # 규칙은 위, 오른쪽, 아래, 왼쪽으로 움직일 때 Y, X-1, Y-1, X-2, Y-2 만큼만 움직인다.

    len_X -= 1                          # 그러니 처음 X 방향으로는 X-1 만큼만 움직여야 한다.
    going_X_r = False
    going_Y_u = True
    going_X_l = False
    going_Y_d = False
    count = 1                           # X나 Y 방향으로 얼마나 갔는지를 확인해야 한다.
    while(person_num <= X * Y):         # 사실 True로 두어도 된다. 찾으면 break하기 때문
        if person_num == person:        # 현재 대기 순서와 입력된 찾고자 하는 값과 같으면
            print(pos_x, end=' ')
            print(pos_y)
            break

        if going_Y_u:
            pos_y += 1
            count += 1
            if count == len_Y:          # Y 방향의 최대 위치까지 가면
                len_Y = len_Y - 1       # 다음에 Y 방향으로 움직일땐 -1 만큼 덜움직인다.
                going_X_r = True        # 다음은 오른쪽 방향
                going_Y_u = False
                count = 0               # count는 다시 0으로 초기화

        elif going_X_r:
            pos_x += 1
            count += 1
            if count == len_X:
                len_X = len_X - 1
                going_Y_d = True
                going_X_r = False
                count = 0

        elif going_Y_d:
            pos_y -= 1
            count += 1
            if count == len_Y:
                len_Y = len_Y - 1
                going_X_l = True
                going_Y_d = False
                count = 0

        elif going_X_l:
            pos_x -= 1
            count += 1
            if count == len_X:
                len_X = len_X - 1
                going_Y_u = True
                going_X_l = False
                count = 0

        person_num += 1