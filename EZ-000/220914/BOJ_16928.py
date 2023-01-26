import sys
input = sys.stdin.readline

from collections import deque


N, M = map(int, input().split())
ladders = {}
snakes = {}
for _ in range(N):
    x, y = map(int, input().split())
    ladders[x] = y
for _ in range(M):
    u, v = map(int, input().split())
    snakes[u] = v

q = deque([1])
cnt = [0] * 101             # 주사위 던진 횟수 저장
visited = [0] * 101         # 칸 방문 여부 저장

while q:
    now = q.popleft()           # 현재 위치는 선입선출
    if now == 100:              # 100에 도착하면
        print(cnt[100])         # 주사위 던진 횟수 출력
        break                   # 반복문 종료
    for n in range(1, 7):
        move = now + n
        if move < 101 and not visited[move]:    # 다음 위치가 100보다 작고 방문하지 않은 칸일 때
            if move in ladders.keys():              # 다음 위치가 사다리면
                move = ladders[move]                    # 다음 위치를 바꿔
            if move in snakes.keys():               # 다음 위치가 뱀이면
                move = snakes[move]                     # 다음 위치를 바꿔

            if not visited[move]:                   # 다음 위치가 여전히 방문하지 않은 칸이면
                visited[move] = 1                       # 방문 표시하고
                cnt[move] = cnt[now] + 1                # 주사위 던진 횟수 저장하고
                q.append(move)                          # 큐에 위치를 저장해!

"""cnt 없이도 가능
import sys
input = sys.stdin.readline

from collections import deque


N, M = map(int, input().split())
ladders = {}
snakes = {}
for _ in range(N):
    x, y = map(int, input().split())
    ladders[x] = y
for _ in range(M):
    u, v = map(int, input().split())
    snakes[u] = v

q = deque([1])
visited = [0] * 101

while q:
    now = q.popleft()
    if now == 100:
        print(visited[100])
        break
    for n in range(1, 7):
        move = now + n
        if move < 101 and not visited[move]:
            if move in ladders.keys():
                move = ladders[move]
            if move in snakes.keys():
                move = snakes[move]

            if not visited[move]:
                visited[move] = visited[now] + 1
                q.append(move)
"""
