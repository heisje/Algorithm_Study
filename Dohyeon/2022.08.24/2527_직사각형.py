testcase = 4
for tc in range(1, testcase + 1):
    result = None

    x1, y1, p1, q1, x2, y2, p2, q2 = list(map(int, input().split()))

    if (x2 - p1) * (p2 - x1) > 0 or (y2 - q1) * (q2 - y1) > 0:
        result = "d" # 공통 x
    elif (x2 - p1) * (p2 - x1) < 0 and (y2 - q1) * (q2 - y1) < 0:
        result = "a" # 직사각형
    elif (x2 - p1) * (p2 - x1) == 0 and (y2 - q1) * (q2 - y1) == 0:
        result = "c" # 점
    elif (x2 - p1) * (p2 - x1) == 0 or (y2 - q1) * (q2 - y1) == 0:
        if (x2 - p1) * (p2 - x1) == 0 and (y2 - q1) * (q2 - y1) > 0:
            result = "d"
        elif (x2 - p1) * (p2 - x1) > 0 and (y2 - q1) * (q2 - y1) == 0:
            result = "d"
        else:
            result = "b" # 선

    print(result)