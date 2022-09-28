import sys

input = lambda: sys.stdin.readline().strip()

N, M = map(int, input().split())
ways = [[] for i in range(N + 1)]

for i in range(M):
    start, end = map(int, input().split())
    ways[start].append(end)
    ways[end].append(start)

visited = [0 for i in range(N + 1)]

count = 0

for i in range(len(visited)):

    if i == 0:          # 0은 인덱스를 위한 존재일뿐
        continue

    if visited[i]:
        continue

    queue = [i]
    start = i

    visited[start] = 1
    while(queue):
        node = queue.pop()

        for w in ways[node]:

            if not visited[w]:
                queue.append(w)
                visited[w] = 1
    count += 1

print(count)



