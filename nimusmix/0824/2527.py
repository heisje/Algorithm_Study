for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
   
    if q1 < y2 or q2 < y1 or p1 < x2 or p2 < x1:
       print('d')
    elif x2 == p1 or x1 == p2:
        if y1 == q2 or y2 == q1:
            print('c')
        else:
            print('b')
    elif y1 == q2 or y2 == q1:
        if x1 == p2 or x2 == p1:
            print('c')
        else:
            print('b')
    else:
        print('a')