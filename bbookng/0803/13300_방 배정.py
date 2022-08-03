import sys

input = lambda: sys.stdin.readline().strip()

n, k = map(int, input().split())

cnt = 0
arr = [[0] * 6 for _ in range(2)]                   # 남,녀 1~6학년 2중 list 생성

for _ in range(n):
    x, y = map(int,input().split())
    arr[x][y-1] += 1                                # x, y값에 따라 리스트의 각 항목에 +1

result = 0
for i in range(2):                                  # 성별을 기준으로 순환
    for j in range(6):                              # 학년을 기준으로 순환
        
         # i성별 j학년의 학생 수에서 한 방에 배정할 수 있는 인원 수인 k 나누기
         # arr[i][j]가 1이상인 경우, k의 배수가 아닌 경우 그냥 몫보다 방이 1개 더 필요 하므로 k-1을 더해서 k로 나눔
        result += (arr[i][j] + k - 1) // k         
        
print(result)