def quater(n, dx, dy):
    temp = [0,0,0,0]
    check = [True,True,True,True]
    for idx, four_y, four_x in [(0, 0, 0), (1, 0, n//2), (2, n//2, 0), (3, n//2, n//2)]:
        temp[idx] = arr[dy][dx]
    
    for idx, four_y, four_x in [(0, 0, 0), (1, 0, n//2), (2, n//2, 0), (3, n//2, n//2)]:
        if temp[idx] == '0': # 0이 기본이면
            other = '1'    # 반대는 1
        if temp[idx] == '1': # 1이 기본이면
            other = '0'    # 반대는 0

        # 1/4 구역이 전부 같은 숫자인지 확인
        check[idx] = True
        for y in range(n//2):
            if other in arr[dy + four_y + y][dx + four_x:dx + four_x + n//2]:
                check[idx] = False
                break
            # for x in range(n//2):
            #     if temp[idx] != arr[dy + four_y + y][dx + four_x + x]: 
            
    
    set_check = set(check)
    if check == [True, True, True, True] and len(set_check) == 1: # 다 똑같으면
        print(temp[0], end='')
    else:
        print('(', end='')
        for idx, four_y, four_x in [(0, 0, 0), (1, 0, n//2), (2, n//2, 0), (3, n//2, n//2)]:
            if check[idx] is True: #같으면
                print(temp[idx], end='')
            if check[idx] is False: # 다르면
                quater(n//2, dx + four_x, dy + four_y)
        print(')', end='')

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(input()))

quater(N, 0, 0)