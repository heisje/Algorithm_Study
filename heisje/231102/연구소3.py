from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline
inf = sys.maxsize

def solution(zCount, dq):
    visited = [[0 for _ in range(N)] for _ in range(N)]

    while dq:
        r, c, count = dq.popleft()
        
        if count >= answer[0]:
            return 
    
        for gr, gc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
            if 0 <= gr < N and 0 <= gc < N :
                if visited[gr][gc] == 0 and (grid[gr][gc] == 0 or grid[gr][gc] == 2):
                    
                    visited[gr][gc] = count + 1
                    dq.append((gr, gc, count + 1))
                    if grid[gr][gc] == 0 :
                        zCount -= 1
                        if zCount <= 0:
                            # print("_------------")
                            # for a in visited:
                            #     print(a)
                            answer[0] = visited[gr][gc]-2
                            return 

N, M = map(int, input().split())
grid = []
points = []
answer = [inf]

zeroCount = 0

for r in range(N):
    temp = list(map(int, input().split()))
    grid.append(temp)
    for c in range(len(temp)):
        if temp[c] == 2:
            points.append((r, c, 2))
        elif temp[c] == 0:
            zeroCount += 1

if zeroCount == 0:
    print(0)
else:

    for point in combinations(points, M):
        solution(zeroCount, deque(point))

    if answer[0] == inf:
        print(-1)
    else:
        print(answer[0])

