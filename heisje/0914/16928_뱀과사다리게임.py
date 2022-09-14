# 아이디어: dp(visited)를 이용해서 node, bfs로 풀기
from collections import deque

N, M = map(int, input().split())
node = [i for i in range(101)]    # node
visited = [0] * 101               # dp로 쓸 visited
for n in range(N):
    start, end = tuple(map(int, input().split())) # node입력
    node[start] = end
for m in range(M):
    start, end = tuple(map(int, input().split())) # node입력
    node[start] = end

dq = deque()
dq.append(1)
while dq:
    now = dq.popleft()
    if now == 100:
        break
    else:
        for dice in range(1,7):
            if 1 <= now + dice <= 100:
                future = node[now + dice]
                if 1 <= future <= 100 and visited[future] == 0:
                    visited[future] = visited[now] + 1
                    dq.append(node[future])
print(visited[100]-1)

# 골드5 / 30분