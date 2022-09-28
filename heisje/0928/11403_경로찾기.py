import sys
input = lambda:sys.stdin.readline()
from collections import deque

N = int(input())
node = []
for _ in range(N):
    node.append(list(map(int, input().split())))

result = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    dq = deque()
    dq.append(i)
    visited = [0] * N
    while dq:
        pre = dq.popleft()
        for idx, value in enumerate(node[pre]):
            if visited[idx] == 0 and value == 1:
                result[i][idx] = 1
                visited[idx] = 1
                dq.append(idx)

for i in range(N):
    print(*result[i])