# import sys
#
# input = sys.stdin.readline
#
# for _ in range(4):
#     x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
#
#     if y2 < y3 or y4 < y1 or x2 < x3 or x4 < x1:
#         print("d")
#     elif (x2 == x3 and y2 == y3) or (x1 == x4 and y1 == y4) or (y1 == y4 and x2 == x3) or (x1 == x4 and y2 == y3):
#         print('c')
#     elif (y1 == y4 and x1 <= x3 <= x2) or (y1 == y4 and x3 <= x1 <= x4) or (y2 == y3 and x1 <= x3 <= x2) or (
#             y2 == y3 and x3 <= x1 <= x4) or (x1 == x4 and y1 <= y3 <= y2) or (x1 == x4 and y3 <= y1 <= y4) or (
#             x2 == x3 and y1 <= y3 <= y2) or (x2 == x3 and y3 <= y1 <= y4):
#         print('b')
#     else:
#         print('a')

# import sys
#
# input = sys.stdin.readline
#
# for _ in range(4):
#     x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
#
#     if y2 < y3 or y4 < y1 or x2 < x3 or x4 < x1:
#         print('d')
#     elif x2 == x3 or x1 == x4:
#         if y2 == y3 or y1 == y4:
#             print('c')
#         elif y1 <= y3 <= y2 or y3 <= y1 <= y4:
#             print('b')
#     elif y1 == y4 or y2 == y3:
#         if x1 <= x3 <= x2 or x3 <= x1 <= x4:
#             print('b')
#     else:
#         print('a')

import sys

input = sys.stdin.readline

for _ in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

    if y2 < y3 or y4 < y1 or x2 < x3 or x4 < x1:    # 꼭짓점을 기준으로 봤을 때 아예 안붙을수가 없는 경우
        print('d')
    elif x2 == x3 or x1 == x4:                      # 오.위 나 왼.아래 두 꼭짓점의 x 좌표가 같고 같은 선상에 있을 때
        if y2 == y3 or y1 == y4:                    # y좌표도 일치하면 점
            print('c')
        else:                                       # 선상에 있기만 하면 선분
            print('b')
    elif y1 == y4 or y2 == y3:                      # 위와 동일한 경우
            print('b')
    else:                                           # 다 아니면 직사각형
        print('a')

