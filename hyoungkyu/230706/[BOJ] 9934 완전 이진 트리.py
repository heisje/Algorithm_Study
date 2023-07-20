# 실버1 / 60ms
import sys
input = sys.stdin.readline

K = int(input())
lst = list(map(int, input().split()))
res = [[] for _ in range(K)]

def inorder(lst, n):
    mid = len(lst)//2
    res[n].append(lst[mid])
    if len(lst) == 1:
        return
    inorder(lst[:mid], n+1)
    inorder(lst[mid+1:], n+1)

inorder(lst, 0)
for i in res:
    print(*i)