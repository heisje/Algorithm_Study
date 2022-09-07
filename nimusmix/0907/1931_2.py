import sys
input = sys.stdin.readline

N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x:(x[1], x[0]))

cnt = 1
prev = meetings[0]

for j in range(1, N):
    if prev[1] <= meetings[j][0]:
        cnt += 1
        prev = meetings[j]

print(cnt)