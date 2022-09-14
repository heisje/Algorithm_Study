# 골드5 / 88ms
import sys
input = lambda: sys.stdin.readline().strip()
from collections import deque

N, M = map(int, input().split())
lst1 = [list(map(int, input().split())) for _ in range(N)]  # 사다리
lst2 = [list(map(int, input().split())) for _ in range(M)]  # 뱀
lst1.sort()
lst2.sort()
visited = [100] * 101
visited[1] = 0
queue = deque()
queue.append(1)
# BFS
while queue:
    flag = False
    t = queue.popleft()
    if t == 100:
        break
    
    # 사다리가 있다면 타고 올라가!
    for xi, xj in lst1:
        if t == xi and visited[xj] > visited[xi]:
            visited[xj] = visited[xi]
            queue.append(xj)
            flag = True
            break
    if flag:
        continue

    # 뱀이 있다면 타고 내려가!
    for yi, yj in lst2:
        if t == yi:
            visited[yj] = visited[yi]
            queue.append(yj)
            flag = True
            break
    if flag:
        continue

    # 사다리, 뱀 둘 다 없다면 주사위 던져서 이동해!
    for i in range(1, 7):
        if t+i<101 and visited[t+i] > visited[t] + 1:
            visited[t+i] = visited[t] + 1
            queue.append(t+i)

print(visited[100])


'''
2번을 안지켜서 계속 틀렸었음ㅠㅠ

1. 모든 칸은 최대 하나의 사다리 또는 뱀을 가지고 있으며, 동시에 두 가지를 모두 가지고 있는 경우는 없다. 하지만 특정한 칸을 도착지점으로 하는 사다리와 뱀의 개수는 두 개 이상일 수 있다.

2. 어떤 칸이 사다리나 뱀의 출발지라면, 반드시 사다리 또는 뱀을 거쳐서만 이동해야 한다. 해당 칸에서는 주사위를 통한 이동을 할 수 없다.
'''