# 88ms

import sys
input = lambda: sys.stdin.readline().strip()
x= int(input())

cnt = 0
for i in range(int(x//2), x+1): # x//2부터 시작인 이유 : 절반보다 작으면 바로 다음에서 끝남
    num = [x]
    num.append(i)
    j = 0
    tmp = 0
    while num[-1] >= 0:  # 음수가 나올때까지 반복
        num.append(num[j] - num[j+1])
        j += 1
    tmp = len(num)
    if tmp > cnt:  # cnt가 개선될때마다 idx 저장
        cnt = len(num) - 1
        lst = num
print(cnt)
lst.pop()
for i in lst:
    print(i, end=' ')
