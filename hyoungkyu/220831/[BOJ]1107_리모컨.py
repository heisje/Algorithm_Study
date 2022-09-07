# 1296ms / 골드5
import sys
input = lambda: sys.stdin.readline().strip()

tar = int(input())
ans = abs(100 - tar)                          
K = int(input())

# exc : 고장난 버튼을 받는 리스트
if K != 0:                                      
    exc = list(input().split())
else:
    exc = []

# 0~1000001까지 완전탐색
for num in range(1000001):
    for i in str(num):      # 버튼을 눌러서 입력할 수 있다면
        if i in exc:
            break
    else:
        ans = min(len(str(tar))+abs(num-tar), ans)  # 최소값 갱신

print(ans)