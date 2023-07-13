import sys
input = sys.stdin.readline

K = int(input())
traversal = [0] + list(map(int, input().split()))

visited = [0 for _ in range(2 ** K)]

step = 2 ** K // 2
while step:
    idx = step
    while idx < 2 ** K:
        if not visited[idx]:
            print(traversal[idx], end=" ")
            visited[idx] = 1
        idx += step
    print()
    step = step // 2
