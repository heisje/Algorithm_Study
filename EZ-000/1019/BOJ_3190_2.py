from collections import deque

N = int(input())
K = int(input())

apples = []
for _ in range(K):
    r, c = map(int, input().split())
    apples.append((r - 1, c - 1))

L = int(input())
D = deque()
R = deque()
for _ in range(L):
    X, C = input().split()
    D.append(int(X))
    R.append(C)

snake = deque([(0, 0)])                     # 뱀의 몸이 차지하는 좌표를 모두 저장
second = 0
order = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
d = 3
delta = {                                   # delta = {현재 방향: {'왼쪽 회전 시': 다음 방향, '오른쪽 회전 시': 다음 방향}}
    0: {'L': 2, 'D': 3},                    # 상
    1: {'L': 3, 'D': 2},                    # 하
    2: {'L': 1, 'D': 0},                    # 좌
    3: {'L': 0, 'D': 1}                     # 우
    }

while True:
    second += 1
    r, c = snake[0]                         # 뱀 머리 좌표
    move = (r + dr[d], c + dc[d])           # 다음 위치
    # 벽이면 중단
    if move[0] < 0 or N - 1 < move[0] or move[1] < 0 or N - 1 < move[1]:
        break
    elif move in snake:                     # 뱀이면 중단
        break
    elif move in apples:                    # 사과면
        apples.remove(move)                     # 사과를 먹고
        snake.appendleft(move)                  # 머리만 이동
    else:                                   # 사과가 아니면
        snake.pop()                             # 꼬리를 제거
        snake.appendleft(move)                  # 머리 이동

    if order < L and second == D[order]:    # 이번 초가 끝난 후 방향 전환
        d = delta[d][R[order]]
        order += 1

print(second)
