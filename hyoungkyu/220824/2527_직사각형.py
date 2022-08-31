# 80ms
import sys
input = lambda: sys.stdin.readline().strip()

def f(rec1, rec2):
    x1, y1, p1, q1 = rec1
    x2, y2, p2, q2 = rec2
    # print(f'x1, y1, p1, q1 = {x1, y1, p1, q1}')             --> 이거 안지우고 계속 제출해서 한시간 날림ㅠㅠ
    # print(f'x2, y2, p2, q2 = {x2, y2, p2, q2}')
    if p1 < x2 or q1 < y2 or y1 > q2:                           # 공통부분 X
        return 'd'
    elif (p1 == x2 and y1 == q2) or (p1 == x2 and q1 == y2) :   # 점
        return 'c'
    elif y1 == q2 or p1 == x2 or q1 == y2:                      # 선분
        return 'b'
    else:                                                       # 직사각형
        return 'a'
for _ in range(4):
    lst = list(map(int, input().split()))
    rec1 = lst[:4]
    rec2 = lst[4:]
    if rec1[0] > rec2[0]:                                       # rec1이 무조건 왼쪽편 직사각형이 되도록
        rec1, rec2 = rec2, rec1

    print(f(rec1, rec2))