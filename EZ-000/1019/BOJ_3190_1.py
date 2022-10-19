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

snake = deque([(0, 0)])
second = 0
order = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
d = 3
delta = {
    0: {'L': 2, 'D': 3},
    1: {'L': 3, 'D': 2},
    2: {'L': 1, 'D': 0},
    3: {'L': 0, 'D': 1}
    }

while True:
    second += 1
    # snake 다음 이동 칸 결정
    r, c = snake[0]
    move = (r + dr[d], c + dc[d])
    # 다음 칸이 벽이면 = 보드의 크기를 넘으면 중단
    if move[0] < 0 or N - 1 < move[0] or move[1] < 0 or N - 1 < move[1]:
        break
    # 다음 칸이 뱀이면 = snake 리스트 안에 있으면 중단
    elif move in snake:
        break
    # apples 리스트에 이동 칸의 좌표가 있으면, 사과를 없애고 꼬리 유지
    elif move in apples:
        apples.remove(move)
        snake.appendleft(move)
    # apples 리스트에 이동 칸의 좌표가 없으면, snake.pop()
    else:
        if snake:
            snake.pop()
        snake.appendleft(move)
    # 이번 초가 끝난 뒤 방향 회전
    if order < L and second == D[order]:
        d = delta[d][R[order]]
        order += 1

print(second)
