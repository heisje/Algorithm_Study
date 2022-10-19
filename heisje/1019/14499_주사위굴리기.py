import sys
input = lambda: sys.stdin.readline()

# 동서남북
d = (
    (1, 0),  #동
    (-1, 0),  #서
    (0, -1),  #남
    (0, 1)   #북
)

dice = {
    'T':0,  # 위
    'B':0,  # 아래
    'N':0,  # 북
    'S':0,  # 남
    'E':0,  # 동
    'W':0,  # 서
}
def dice_rotate(way, dice):    
    if way == 2:  #서
        dice = {
            # N, S 안바뀜
            'T': dice['E'],  # 위
            'B': dice['W'],  # 아래
            'E': dice['B'],  # 동
            'W': dice['T'],  # 서
            'N': dice['N'],  # 북
            'S': dice['S'],  # 남
        }
    elif way == 1:  #동
        dice = {
            # N, S 안바뀜
            'T': dice['W'],  # 위
            'B': dice['E'],  # 아래
            'E': dice['T'],  # 동
            'W': dice['B'],  # 서
            'N': dice['N'],  # 북
            'S': dice['S'],  # 남
        }
    elif way == 4:  #북
        dice = {
            # E, W제외
            'T': dice['S'],  # 위
            'B': dice['N'],  # 아래
            'N': dice['T'],  # 북
            'S': dice['B'],  # 남
            'E': dice['E'],  # 
            'W': dice['W'],  # 
        }
    elif way == 3:  #남
        dice = {
            # E, W제외
            'T': dice['N'],  # 위
            'B': dice['S'],  # 아래
            'N': dice['B'],  # 북
            'S': dice['T'],  # 남
            'E': dice['E'],  # 
            'W': dice['W'],  # 
        }
    return dice
N, M, y, x, K = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))
rotates = list(map(int, input().split()))
for way in rotates:
    # 방향대로 굴린다
    go_x = x + d[way-1][0]
    go_y = y + d[way-1][1]

    # 지도에서 벗어나면 무시한다.
    if go_x < 0 or M <= go_x or go_y < 0 or N <= go_y:
        continue

    # 지도에서 벗어나지 않았으면 굴린다.
    dice = dice_rotate(way, dice)
    # T을 표시한다.
    print(dice['T'])

    # 지도를 확인하여 0이면
    if grid[go_y][go_x] == 0:
        grid[go_y][go_x] = dice['B']
    else:  # 0이 아니면
        dice['B'] = grid[go_y][go_x]
        grid[go_y][go_x] = 0
    
    x, y = go_x, go_y
# 골드4 / 60분