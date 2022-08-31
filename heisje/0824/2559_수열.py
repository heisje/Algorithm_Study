#import sys
#sys.stdin = open('input.txt')

#DP였네 . . . . . . .
#풀이 : 첫번째 온도의 합계를 구하고, 
#       두번째 온도는 가장 왼쪽값을 빼고 오른쪽 값을 더하면 도니다.
N, K = map(int, input().split())

arr = list(map(int, input().split()))

dp = [0] * (N - K + 1) #dp개수만큼 만들기

dp[0] = sum(arr[0:0+K])#첫번째 합계값 저장
for n in range(1, N-K+1):
    dp[n] = dp[n-1] - arr[n-1] + arr[n+K-1] #지난 dp에 제일 왼쪽값 빼고 오른쪽값 더하기
print(max(dp))