import sys
sys.stdin = open('input.txt')

for _ in range(4):
    lx1, ly1, rx1, ry1, lx2, ly2, rx2, ry2 = map(int, input().split())

    box1_x = [lx1, rx1] # 박스1의 왼쪽 x ~ 오른쪽 x
    box1_y = [ly1, ry1] # 박스1의 왼쪽 y ~ 오른쪽 y

    box2_x = [lx2, rx2] # 박스2의 왼쪽 x ~ 오른쪽 x
    box2_y = [ly2, ry2] # 박스2의 왼쪽 y ~ 오른쪽 y

    # 1. range로 box?_? 사이값을 다 채워준다.
    # 2. set으로 만들어 교집합을 시켜준다.
    # 3. 리스트에 겹치는 x와 겹치는 y를 받는다.
    x = list(set(range(box1_x[0], box1_x[1] + 1)) & set(range(box2_x[0], box2_x[1] + 1)))
    y = list(set(range(box1_y[0], box1_y[1] + 1)) & set(range(box2_y[0], box2_y[1] + 1)))

    if len(x) == 0 or len(y) == 0: # 만약 x y 중 하나가 교집합이 없으면
        print('d')
    elif len(x) == 1 and len(y) == 1: # 만약 x y 둘 다 점 1개만 교집합이면
        print('c')
    elif (len(x) == 1 and len(y) > 1) or (len(x) > 1 and len(y) == 1): #한 쪽만 1개의 교집합을 가질때
        print('b')
    else: #나머지 겹칠 때
        print('a')