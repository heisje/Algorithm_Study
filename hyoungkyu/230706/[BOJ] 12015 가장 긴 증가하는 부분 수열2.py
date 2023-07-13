# 골드2 / 1972ms
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

res_lst = [0]

def func(tar):
    s, e = 0, len(res_lst)
    while s<e:
        m = (s+e)//2
        if tar > res_lst[m]:
            s = m+1
        else:
            e = m
    return e

for a in A:
    if res_lst[-1] < a:
        res_lst.append(a)
    else:
        res_lst[func(a)] = a
# print(res_lst[1:])
print(len(res_lst[1:]))
