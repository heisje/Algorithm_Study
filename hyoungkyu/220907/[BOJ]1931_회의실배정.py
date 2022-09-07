# 실버1 / 368ms
import sys
input = lambda:sys.stdin.readline().strip()

N = int(input())
lst = []
for _ in range(N):
    S, E = map(int, input().split())
    lst.append([S, E])
lst.sort()
# [[1, 3], [2, 2], [3, 4], [4, 4], [5, 8], [6, 8], [7, 8], [8, 8], [9, 10], [10, 10]]
visited = [lst[0]]
i = 1
j = 0                                   # lst에서 visited[-1] 값의 인덱스
while i != N:
    if lst[i][1] < visited[-1][1]:      # 뒤의 숫자가 앞의 숫자에 포함될 경우
        visited.pop()
        visited.append(lst[i])
        j = i
        i -= 1
    elif lst[i][0] >= visited[-1][1]:   # 뒤의 숫자가 입력 가능한 시간이면
        if i != j:                      # ex) [13, 13]인 경우 2번 입력이 되므로 중복입력을 막기 위해서
            visited.append(lst[i])
            j = i
            i += 1
        else:                           # 중복입력인 경우
            i += 1
    elif lst[i][0] < visited[-1][1]:    # 시간이 겹치는 경우
        i += 1

print(len(visited))
