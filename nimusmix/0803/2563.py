n = int(input())
paper = [[0] * 100 for _ in range(100)]        # 전체 도화지 크기의 이차원 리스트 생성

for _ in range(n):
    a, b = map(int, input().split())
    
    for i in range(b, b+10):                   # 입력 받은 가로와 세로 만큼의 범위를 1로 변경
        for j in range(a, a+10):
            paper[i][j] = 1
            
cnt = 0
for i in paper:                                # 전체 1의 합계 출력
    cnt += sum(i)
            
print(cnt)