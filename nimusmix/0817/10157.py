X, Y = map(int, input().split())
N = int(input())
hall = [[0] * X for _ in range(Y)]

x, y = 0, Y-1
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
dr = 0
cnt = 1

hall[y][x] = cnt

while cnt < X*Y:    
    nx = x + dx[dr]
    ny = y + dy[dr]
    if 0 <= nx < X and 0 <= ny < Y and hall[ny][nx] == 0:
        x, y = nx, ny
        cnt += 1
        hall[y][x] = cnt
    else:
        dr = (dr+1) % 4
        
for idx, i in enumerate(hall):
    if N > X*Y:
        print(0)
        break
    elif N in i:
        row = i.index(N)+1
        col = Y - idx
        print(row, col)
for i in hall:
    print(*i)