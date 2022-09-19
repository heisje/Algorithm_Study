from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()
T = int(input())

def bfs():
    queue = deque()
    queue.append(A)
    visited[A] = 0

    while queue:
        V = queue.popleft()

        # D
        tmp = V*2%10000
        if visited[tmp] == -1:
            queue.append(tmp)
            visited[tmp] = V
            oper[tmp] = 'D'
            if tmp == B: return

        # S
        if V == 0: tmp = 9999
        else: tmp = V-1
        if visited[tmp] == -1:
            queue.append(tmp)
            visited[tmp] = V
            oper[tmp] = 'S'
            if tmp == B: return
 
        if V != 0:
            # L
            other = V % 1000
            one = V // 1000
            tmp = other * 10 + one
            if visited[tmp] == -1:
                queue.append(tmp)
                visited[tmp] = V
                oper[tmp] = 'L'
                if tmp == B: return

            # R
            other = V // 10
            one = V % 10
            tmp = one * 1000 + other
            if visited[tmp] == -1:
                queue.append(tmp)
                visited[tmp] = V
                oper[tmp] = 'R'
                if tmp == B: return

for _ in range(T):
    A, B = map(int, input().split())
    visited = [-1] * 10001
    oper = [''] * 10001
    ans = deque()
    bfs()
    tmp = B
    
    while oper[tmp] != '':
        ans.appendleft(oper[tmp])
        tmp = visited[tmp]
        
    print(*ans, sep='')