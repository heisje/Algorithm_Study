import sys
input = sys.stdin.readline
from collections import deque

def move(direction):
    # 상
    if not direction:
        for j in range(N):
            for i in range(N):
                if arr[i][j]:                       # 0이 아니면 q에 담아주기
                    q.append(arr[i][j])

            for i in range(N):
                if len(q) > 1:                      # q에 2개 이상 있으면
                    if q[0] == q[1]:                # 연속 2개가 같으면
                        arr[i][j] = q.popleft() * 2 # merge 해서 값 넣어주고 하나 빼고
                        q.popleft()                 # 하나 빼기
                    else:                           # 안같으면
                        arr[i][j] = q.popleft()     # 젤 앞에거 일단 빼기
                elif q:                             # q에 하나만 남았으면
                    arr[i][j] = q.popleft()         # 칸 채우기
                else:                               # q에 아무 것도 없으면 N번 반복에서 남은 횟수만큼
                    arr[i][j] = 0                   # 0 으로 채워주기

    # 하
    if direction == 1:
        for j in range(N):
            for i in range(N-1, -1, -1):
                if arr[i][j]:
                    q.append(arr[i][j])
            for i in range(N):
                if len(q) > 1:
                    if q[0] == q[1]:
                        arr[N-i-1][j] = q.popleft() * 2
                        q.popleft()
                    else:
                        arr[N-i-1][j] = q.popleft()
                elif q:
                    arr[N-i-1][j] = q.popleft()
                else:
                    arr[N-i-1][j] = 0

    # 좌
    if direction == 2:
        for i in range(N):
            for j in range(N):
                if arr[i][j]:
                    q.append(arr[i][j])

            for j in range(N):
                if len(q) > 1:
                    if q[0] == q[1]:
                        arr[i][j] = q.popleft() * 2
                        q.popleft()
                    else:
                        arr[i][j] = q.popleft()
                elif q:
                    arr[i][j] = q.popleft()
                else:
                    arr[i][j] = 0

    # 우
    if direction == 3:
        for i in range(N):
            for j in range(N-1, -1, -1):
                if arr[i][j]:
                    q.append(arr[i][j])

            for j in range(N):
                if len(q) > 1:
                    if q[0] == q[1]:
                        arr[i][N-j-1] = q.popleft() * 2
                        q.popleft()
                    else:
                        arr[i][N-j-1] = q.popleft()
                elif q:
                    arr[i][N-j-1] = q.popleft()
                else:
                    arr[i][N-j-1] = 0


def solve(idx):
    global arr, answer
    if idx == 5:                                        # 5번 했을 때 최댓값 구하기
        for i in range(N):
            answer = max(answer, max(arr[i]))
        return

    b = [x[:] for x in arr]                             # arr을 복사해 둘 list

    for k in range(4):                                  # 네 방향 탐색
        move(k)
        solve(idx + 1)
        arr = [x[:] for x in b]                         # 재귀에서 빠져 나오면 다시 arr 그 전 상태로 돌리기

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque()
answer = 0
solve(0)

print(answer)