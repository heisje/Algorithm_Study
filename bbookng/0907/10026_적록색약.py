import sys
input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(10000)

N = int(input())
board = [list(input()) for _ in range(N)]
visitied = [[0] * N for _ in range(N)]

cnt1 = 0                                                            # 적록색약 아닐 때
cnt2 = 0                                                            # 적록색약 일 때

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visitied[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and visitied[nx][ny] == 0:
            if board[x][y] == board[nx][ny]:                        # 구역 달라질 때 까지
                dfs(nx, ny)

for i in range(N):
    for j in range(N):
        if visitied[i][j] == 0:                                     # visited 0인 지점 찾아서 구역 찾기
            dfs(i, j)                                               # 한 번 실행되면 한 구역 돌고 나오고
            cnt1 += 1                                               # count +1 해줍니다

for i in range(N):                                                  # 적록색약 일 때 구분 안가니까
    for j in range(N):                                              # 똑같은걸로 만들어줘버리기
        if board[i][j] == 'R':
            board[i][j] = 'G'

visitied = [[0] * N for _ in range(N)]                              # visited table 초기화

for i in range(N):                                                  # 마찬가지
    for j in range(N):
        if visitied[i][j] == 0:
            dfs(i, j)
            cnt2 += 1

print(cnt1, cnt2)





