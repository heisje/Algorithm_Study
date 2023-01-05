import sys
input = sys.stdin.readline

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def solution(x, y, d):
    arr[x][y] = 2       # 로봇청소기 처음 자리 청소
    result = 1          # 하나 청소 완

    while True:
        for _ in range(4):      # 4 방향 탐색
            d = (d + 3) % 4     # 현재 방향 기준 왼쪽 바라보는 방향
            nx, ny = x + directions[d][0], y + directions[d][1]     # new
            if 0 <= nx < N and 0 <= ny < M and not arr[nx][ny]:     # 범위 안 and 청소 X
                arr[nx][ny] = 2                                     # 청소
                result += 1                                         # + 1
                x, y = nx, ny                                       # 현재 자리로 설정
                break                                               # 청소했으면 다시 for 문 멈추고 while 문으로
        else:                                                       # 4 방향 다 돌고도 청소 못했으면
            x, y = x - directions[d][0], y - directions[d][1]       # 후진
            if arr[x][y] == 1:                                      # 벽이면
                return result                                       # 끝

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(solution(r, c, d))