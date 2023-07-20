# 골드5 / 484ms
import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
lst_1 = []
lst_2 = []

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 1:
            lst_1.append((i, j))
        elif tmp[j] == 2:
            lst_2.append((i, j))

def get_distance(lst):  # [i1, j1, i2, j2]
    return abs(lst[0]-lst[2]) + abs(lst[1]-lst[3])

def func():
    minV = float('inf')
    for comb in combinations([i for i in range(len(lst_2))], M):
        visited = [float('inf')] * len(lst_1)
        for idx in comb:
            for k in range(len(lst_1)):
                tmp = lst_2[idx] + lst_1[k]
                visited[k] = min(visited[k], get_distance(tmp))
        minV = min(minV, sum(visited))
    return minV

# def func(idx_lst, minV):
#     if len(idx_lst) == M:
#         visited = [float('inf')] * len(lst_1)
#         for idx in idx_lst:
#             for k in range(len(lst_1)):
#                 tmp = lst_1[k] + lst_2[idx]
#                 visited[k] = min(visited[k], get_distance(tmp))
#         return sum(visited)
#     for i in range(len(lst_2)):
#         if i not in idx_lst:
#             minV = min(minV, func(idx_lst+[i], minV))
#     return minV

# print(func([], float('inf')))
print(func())