import sys
input = lambda: sys.stdin.readline().strip()

w, h = map(int, input().split())                # 돌아다닐 수 있는 판의 x, y
pos_x, pos_y = map(int, input().split())        # 초기 위치

t = int(input())                                # 시간


if w - pos_x >= t:                              # 초기 x좌표 위치가 시간만큼 움직여도 벽에 닿지 않을 경우
    pos_x = pos_x + t                           # 최종 x좌표 위치
else:                                           # 벽에 닿을 만큼 시간이 넉넉한 경우
    tx = t - (w - pos_x)                        # 벽에 닿았을 때의 남은 시간을 구한다
    move_w = tx // w                            # 남은시간에 가로 길이를 나눈 몫을 통해 몇 번 닿는지 확인
    x_d = tx % w                                # 나머지 값을 통해 위치를 특정
    if move_w % 2 == 0:                         # 짝수번일 경우 오른쪽에서 나머지 만큼 떨어짐
        pos_x = w - x_d
    else:                                       # 홀수번일 경우 왼쪽에서 나머지 만큼 떨어짐
        pos_x = x_d
                                                # y좌표도 같은 방법으로 해결
if h - pos_y >= t:
    pos_y = pos_y + t
else:
    ty = t - (h - pos_y)
    move_h = ty // h
    y_d = ty % h
    if move_h % 2 == 0:
        pos_y = h - y_d
    else:
        pos_y = y_d

print(pos_x, end=' ')
print(pos_y)

