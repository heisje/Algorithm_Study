# 68ms
from collections import deque

def main():
    dq = deque()
    dq.append((0, len(li)-1, 0, 1))
    while dq:
        left, right, depth, rightFlag = dq.popleft()
        center = left + (right - left) // 2
        if rightFlag:
            print(li[center])
        else:
            print(li[center], end=' ')
        if left == right:
            continue
        dq.append((left, center - 1, depth + 1, 0))
        if rightFlag == 0:
            dq.append((center + 1, right, depth + 1, 0))
        else:
            dq.append((center + 1, right, depth + 1, 1))
            

N = int(input())
li = list(map(int, input().split()))
main()
