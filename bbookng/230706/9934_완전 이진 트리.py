import sys
input = sys.stdin.readline
from collections import deque

K = int(input())
inorder = list(map(int, input().split()))
ans = [[] for _ in range(K)]

def solution1(arr, d):
    q = deque([(inorder, 0)])

    while q:
        arr, d = q.popleft()
        mid = len(arr) // 2
        ans[d].append(arr[mid])
        if len(arr) != 1:
            q.append((arr[:mid], d+1))
            q.append((arr[mid+1:], d+1))

def solution2(arr, d):
    mid = len(arr) // 2
    ans[d].append(arr[mid])

    if len(arr) == 1:
        return

    solution2(arr[:mid], d+1)
    solution2(arr[mid+1:], d+1)

solution2(inorder, 0)

for i in ans:
    print(*i)