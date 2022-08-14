W, H=map(int, input().split())
FIND = int(input())

   #(y, x)#위      #우     #하      #좌
direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dir = 0
MAX = W * H #최대값

x = y = 0 #현재위치
count = 1 #숫자
W_0 = H_0 = 0

grid = [[0] * W for _ in range(H)] #보조도구 맵
for count in range(1, MAX + 1): #1부터 42까지 출력
    grid[y][x] = count
    if count == FIND: #종료조건
        print(x + 1, y + 1)
        break
    go_x = x + direct[dir % 4][1] #갈 위치
    go_y = y + direct[dir % 4][0] 
    if W_0 <= go_x < W and H_0 <= go_y < H and grid[go_y][go_x] == 0 : #안에 있으면
        pass
    else:
        dir += 1 
    x += direct[dir % 4][1]
    y += direct[dir % 4][0]
    #for h in range(H):    #맵보기
    #    print(*grid[h])
else:
    print(0)
