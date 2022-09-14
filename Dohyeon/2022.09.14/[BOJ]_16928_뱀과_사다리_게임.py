import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

ways = {}

for i in range(94):
    ways[i + 1] = [i + 2, i + 3, i + 4, i + 5, i + 6, i + 7]
ways[95] = [96, 97, 98, 99, 100]
ways[96] = [97, 98, 99, 100]
ways[97] = [98, 99, 100]
ways[98] = [99, 100]
ways[99] = [100]

shoong = {}
for i in range(N + M):
    start, end = map(int, input().split())
    shoong[start] = end

key_sh = list(shoong.keys())

def BFS(start, target):
    queue = deque([start])
    distance = [0]*101 # distance로 방문 여부와 소요 시간을 함께 저장 인덱스 에러 방지 +1 만큼 더 만듦

    while queue:
        node = queue.popleft()
        for next in ways[node]:
            if next > 100:
                continue
            if distance[next]:              # BFS니까 이전 단계에서 만든 경로가 더 짧을 수 밖에 없다.
                continue
            if next in key_sh:
                if distance[shoong[next]]:
                    continue
            if next == target :
                return distance[node] + 1
            else:
                if next in key_sh:
                    queue.append(shoong[next])
                    distance[shoong[next]] = distance[node] + 1
                    distance[next] = distance[node] + 1
                else:
                    queue.append(next)
                    distance[next] = distance[node] + 1

print(BFS(1, 100))