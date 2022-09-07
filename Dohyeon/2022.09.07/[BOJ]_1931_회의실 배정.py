import sys
input = sys.stdin.readline
N = int(input())
meeting_list = {}
# 그리디하게 풀자
for i in range(N):
    start, end = map(int, input().split())
    try:
        meeting_list[end].append(start)

    except KeyError:
        meeting_list[end] = [start]

for key in meeting_list.keys():
    meeting_list[key].sort()


keys_list = list(meeting_list.keys())   # 키는 회의가 끝나는 시간이다.
keys_list.sort()

count = 1
now = keys_list[0]
is_every = True
if len(meeting_list[keys_list[0]]) == 1:
    is_every = False
else:
    for i in meeting_list[keys_list[0]]:
        if now == i:
            count += 1
        else:
            is_every = False
if is_every:
    count -= 1

for i in range(len(keys_list) - 1):
    for j in meeting_list[keys_list[i + 1]]:
        if now <= j:
            count += 1
            now = keys_list[i + 1]
    else:
        continue
print(count)