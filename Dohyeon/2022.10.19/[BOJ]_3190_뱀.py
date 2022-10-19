N = int(input())
K = int(input())

apples = {}
for i in range(K):
    r, c = map(int, input().split())
    r = r - 1
    c = c - 1
    try:
        apples[r].append(c)         # 나중에 특정 행에서는 그 행(딕셔너리 키값)에 존재하는 열만 조심할 예정이다.
    except KeyError:
        apples[r] = [c]

L = int(input())

turn = {}
for i in range(L):
    t, d = input().split()
    t = int(t)
    turn[t] = d

time = 0
direction = 0
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
snake = [[0, 0]]
while(True):
    eat_apple = False
    time += 1
    head = snake[0]
    next = [head[0] + di[direction]] + [head[1] + dj[direction]]
    if next[0] == -1 or next[0] == N or next[1] == -1 or next[1] == N:  # 벽이면 나온다
        break
    if next in snake:
        break
    try:
        for i in range(len(apples[next[0]])):
            if next[1] == apples[next[0]][i]:
                eat_apple = True
                apples[next[0]].pop(i)
                break
    except KeyError:
        pass
    snake.insert(0, next)
    if eat_apple:
        pass
    else:
        snake.pop()

    try:
        if turn[time] == "L":
            direction -= 1
            if direction == -1:
                direction = 3
        elif turn[time] == "D":
            direction += 1
            if direction == 4:
                direction = 0
    except KeyError:
        pass

print(time)


