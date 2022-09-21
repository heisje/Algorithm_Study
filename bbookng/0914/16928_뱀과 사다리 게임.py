import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [i for i in range(101)]                     # 해당 칸의 위치를 넣어줌
visited = [0] * 101

for _ in range(N+M):
    x, y = map(int, input().split())
    graph[x] = y                                    # 뱀 또는 사다리 인 경우에는 갈 위치 변경


def bfs():
    q = deque([1])
    while q:
        now = q.popleft()                           # 현재 위치
        for i in range(1, 7):                       # 주사위 면의 갯수
            next = now + i                          # 다음 위치
            if next <= 100:                         # 범위 안에서
                tmp = graph[next]                   # 주사위 도착해서 다음 갈 곳
                if visited[tmp] == 0:               # 방문하지 않은 곳이라면
                    q.append(tmp)                   # 탐색하기 위해 q에 추가
                    visited[tmp] = visited[now] + 1 # 횟수 추가
                    if tmp == 100:                  # 도달하면
                        return visited[100]         # 값 반환



print(bfs())