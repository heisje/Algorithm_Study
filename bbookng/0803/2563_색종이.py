import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())

board = [[0] * 100 for _ in range(100)]         # 100x100 도화지 생성

for _ in range(n):
    i, j = map(int,input().split())             
    for x in range(i, i+10):                    # 입력받은 수 기준으로 변의 길이 10 만큼
        for y in range(j, j+10):                # board에 해당 넓이 만큼 1로 만들어줌.
            board[x][y] = 1

result = 0

for i in range(len(board)):                     # 1인 항목들의 갯수만큼 result에 저장.
    result += sum(board[i])

print(result)

