board = [[0] * 100 for _ in range(100)]           # 전체 보드 크기의 이차원 리스트 생성

for i in range(4):
    a, b, c, d = map(int, input().split())
    
    for j in range(a, c):                         # x축 범위를 순회
        for k in range(b, d):                     # y축 범위를 순회
            board[j][k] = 1                       # 입력 받은 만큼의 범위를 1로 변경

cnt = 0
for l in board:                                   # 전체 1의 합계 출력
    cnt += sum(l)
    
print(cnt)