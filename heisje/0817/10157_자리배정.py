#https://www.acmicpc.net/problem/10157

#핵심: 달팽이를 그린다. 근데 그리다가 찾는 번호가 나오면 종료

W, H=map(int, input().split())
FIND = int(input())

   #(y, x)#위      #우     #하      #좌
go = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dir = 0   #방향 저장
MAX = W * H #최대값

x = y = 0 #현재위치
count = 1 #숫자

#최대 숫자보다 크면 종료
if FIND > MAX:
    print(0)
    exit()

#그냥 달팽이 그리기
grid = [[0] * W for _ in range(H)] #보조도구 맵
for count in range(1, MAX + 1): #1부터 42까지 출력
    grid[y][x] = count
    if count == FIND: #종료조건
        print(x + 1, y + 1)
        break
    go_x = x + go[dir % 4][1] #갈 위치
    go_y = y + go[dir % 4][0] 
    if 0 <= go_x < W and 0 <= go_y < H and grid[go_y][go_x] == 0 : #안에 있고, 0이면
        pass
    else:  #안에 없고, 이미 숫자가 있으면
        dir += 1 
    x += go[dir % 4][1]
    y += go[dir % 4][0]
