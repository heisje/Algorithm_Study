from collections import deque, defaultdict
from copy import deepcopy

N, M = map(int, input().split())

relation = defaultdict()
for _ in range(M):
    p1, p2 = map(int, input().split())
    if p1 in relation.keys():
        relation[p1] += [p2]
    else:
        relation[p1] = [p2]
    
    if p2 in relation.keys():
        relation[p2] += [p1]
    else:
        relation[p2] = [p1]

kv = sum([n for n in range(N)])
insider = 0
for p in range(N, 0, -1):
    visited = []
    temp_kv = 0
    visited.append(p)
    q1 = deque()
    q2 = []
    q1.append(p)
    depth = 1
    while q1:
        node = q1.popleft()
        for e in relation[node]:
            if e not in visited:
                visited.append(e)
                q2.append(e)
                temp_kv += depth
        if list(q1) == []:
            q1 = deque(deepcopy(q2))
            q2 = []
            depth += 1

    if temp_kv <= kv:
        kv = temp_kv
        insider = p

print(insider)
