N = int(input())
meetings = []
for _ in range(N):
    S, E = map(int, input().split())
    meetings += [[S, E]]

meetings.sort(key=lambda x: x[0])
meetings.sort(key=lambda x: x[1])

cnt = 1
E = meetings[0][1]
for i in range(1, N):
    if E <= meetings[i][0]:
        cnt += 1
        E = meetings[i][1]

print(cnt)

'''mini_log
[참고] https://hongcoding.tistory.com/22
'''