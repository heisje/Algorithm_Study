N = int(input())

dp = [5] * (N+1)                    # 최대 4개까지니까 기본값 5로 설정
dp[0] = 0
dp[1] = 1
for i in range(2, N+1):             # dp table 채우기
    _min = 5                        # 최솟값 초기화
    j = 1                           # 제곱수를 만들 j 초기화
    while i - j ** 2 >= 0:
        _min = min(_min, dp[i-j**2]+1)    # i-j**2의 최솟값 + 1 한것이 최솟값보다 작다면 갱신
        if _min == 1:               # 만약 최솟값이 1이면 더이상 작아질 수 없으므로 break
            break
        j += 1                      # j += 1

    dp[i] = _min                    # 탐색이 끝난 후 최솟값을 dp 테이블에 저장

print(dp[N])
#
# # python3로 어케하노 해서 찾아봤는데 훨씬 간단한 방법이 있었삼
# def f(n):
#   if int(n**0.5)==n**0.5:
#     return 1
#   for i in range(1,int(n**0.5)+1):
#     if int((n-i**2)**0.5)==(n-i**2)**0.5:
#       return 2
#   for i in range(1,int(n**0.5)+1):
#     for j in range(1,int((n-i**2)**0.5)+1):
#       if int((n-i**2-j**2)**0.5)==(n-i**2-j**2)**0.5:
#         return 3
#   return 4
# print(f(int(input())))