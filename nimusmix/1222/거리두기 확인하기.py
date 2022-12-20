from itertools import combinations
from collections import deque

def bfs(i, j, tmp):
    visited = [[0] * len(tmp[0]) for _ in range(len(tmp))]
    visited[i][j] = 1
    queue = deque()
    queue.append((i, j))
    
    while queue:
        si, sj = queue.popleft()
        
        if (si != i or sj != j) and tmp[si][sj] == 'P':
            return 0
        
        for di, dj in [(0, 1), (1, 0), (0, -1)]:
            mi, mj = si + di, sj + dj
            if 0 <= mi < len(tmp) and 0 <= mj < len(tmp[0]) and visited[mi][mj] == 0 and tmp[mi][mj] != 'X':
                visited[mi][mj] = 1
                queue.append((mi, mj))
    return 1


def check(place):
    person = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                person.append((i, j))

    for combi in combinations(person, 2):
        si, sj = combi[0]
        vi, vj = combi[1]

        if abs(si - vi) + abs(sj - vj) < 3:
            print((si, sj), (vi, vj))
            # for i in place:
            #     print(i)
            tmp = [i[min(sj, vj):max(sj, vj) + 1] for i in place[min(si, vi):max(si, vi) + 1]]
            for i in tmp:
                print(i)
            print()
            for i in range(len(tmp)):
                for j in range(len(tmp[0])):
                    if tmp[i][j] == 'P':
                        rst = bfs(i, j, tmp)
                        break
                    if rst == 0:
                        return 0
    return 1

def solution(places):
    ans = [0] * 5
    for i in range(5):
        ans[i] = check(places[i])
    return ans



print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
# print(solution([["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"]]))