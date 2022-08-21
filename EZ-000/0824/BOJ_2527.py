import sys


def overlap(x1, y1, p1, q1, x2, y2, p2, q2):
    if p2 < x1 or p1 < x2 or q1 < y2 or q2 < y1:
        return 'd'
    elif (x1 == p2 and (y1 == q2 or y2 == q1)) or (x2 == p1 and (y1 == q2 or y2 == q1)):
        return 'c'
    elif x1 == p2 or x2 == p1 or y1 == q2 or y2 == q1:
        return 'b'
    else:
        return 'a'


for _ in range(4):
    X1, Y1, P1, Q1, X2, Y2, P2, Q2 = map(int, sys.stdin.readline().split())
    print(overlap(X1, Y1, P1, Q1, X2, Y2, P2, Q2))

'''mini_log
참고 1. https://itcrowd2016.tistory.com/85
참고 2. https://devlibrary00108.tistory.com/359
'''
