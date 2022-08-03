N, K = map(int,input().split())
l = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]] 
# 1학년 ~ 6학년 리스트 안에 [여, 남] 리스트 생성

for i in range(N):
    s, y = map(int, input().split())
    l[y-1][s] += 1  # 학년, 성별에 맞는 리스트의 값 +1
count = 0
for i in l:
    if i[0] % K == 0:  # 딱 맞아 떨어지는 경우
        count += i[0] // K
    else:  # 딱 맞아 떨어지지 않는 경우
        count += (i[0] // K) + 1

    if i[1] % K == 0:
        count += i[1] // K
    else:
        count += (i[1] // K) + 1
        
print(count)