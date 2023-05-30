from collections import deque

a, b, c = map(int, input().split())

answer = []
visited = [[0] * (b+1) for _ in range(a+1)]
q = deque([[0, 0, c]])
visited[0][0] = 1

def check(x, y):
    if not visited[x][y]:
        visited[x][y] = 1
        q.append([x, y, c-x-y])

def solution():
    while q:
        A, B, C = q.popleft()

        if A == 0:
            answer.append(C)

        # C -> A
        if A + C <= a:
            check(A+C, B)
        else:
            check(a, B)

        # C -> B
        if B + C <= b:
            check(A, B+C)
        else:
            check(A, b)

        # A -> B
        if A + B <= b:
            check(0, A+B)
        else:
            check(A-(b-B), b)

        # A -> C
        if A + C <= c:
            check(0, B)
        else:
            check(A-(c-C), B)

        # B -> A
        if A + B <= a:
            check(A+B, 0)
        else:
            check(a, B-(a-A))

        # B -> C
        if B + C <= c:
            check(A, 0)
        else:
            check(A, B-(c-C))

solution()
answer.sort()

for i in answer:
    print(i, end=' ')
