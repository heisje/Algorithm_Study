import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

wheels = [deque(map(int, str(input()))) for _ in range(4)]
K = int(input())

for _ in range(K):
    N, D = map(int, input().split())
    N = N - 1                                                         # 인덱스가 0부터 시작하므로 1을 빼줌.
    
    if 0 <= N-1 and wheels[N][6] != wheels[N-1][2]:                   # N보다 작은 번호의 톱니바퀴 회전
        if 0 <= N-2 and wheels[N-1][6] != wheels[N-2][2]:
            if 0 <= N-3 and wheels[N-2][6] != wheels[N-3][2]:
                wheels[N-3].rotate(-D)
            wheels[N-2].rotate(D)
        wheels[N-1].rotate(-D)

    if N+1 < 4 and wheels[N][2] != wheels[N+1][6]:                    # N보다 큰 번호의 톱니바퀴 회전
        if N+2 < 4 and wheels[N+1][2] != wheels[N+2][6]:
            if N+3 < 4 and wheels[N+2][2] != wheels[N+3][6]:
                wheels[N+3].rotate(-D)
            wheels[N+2].rotate(D)
        wheels[N+1].rotate(-D)

    wheels[N].rotate(D)                                               # N 회전

score = 0
for i in range(4):
    score += 2 ** i if wheels[i][0] else 0

print(score)