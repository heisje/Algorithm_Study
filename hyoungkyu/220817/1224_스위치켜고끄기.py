# 68ms

import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())
switch = list(map(int, input().split()))

# 남 -> 자기가 받은 수의 배수에 해당하는 스위치를 바꿈
# 여 -> 자기가 받은 수의 좌우 대칭이 가장 많은 스위치를 포함하는 구간의 스위치를 바꿈 (항상 홀수)

for _ in range(int(input())):
    a, b = map(int, input().split())

    # 남자일 경우
    if a == 1:                                          
        for i in range(b-1, N, b):                  # b의 배수 부분을 다 바꿈
            if switch[i] == 1:
                switch[i] = 0
            else:
                switch[i] = 1
    
    # 여자일 경우
    else:
        maxV = 0                                    # 양 옆 몇칸까지 바꿀지 받는 변수
        if b <= (N // 2):                           # 카드의 개수(N)의 왼쪽부분인 경우
            for k in range(b):                      # k 범위 설정
                if switch[b-1-k] == switch[b-1+k]:  # 해당 카드부터 한칸씩 양 옆이 같은지 확인
                    maxV = k                        # 같으면 maxV 갱신
                else:                               # 다르면 break
                    break
            for j in range(b-1-maxV, b+maxV):       # 회문 구간 바꾸기
                if switch[j] == 1:
                    switch[j] = 0
                else:
                    switch[j] = 1

        else:
            for k in range(N - b + 1):
                if switch[b-1-k] == switch[b-1+k]:
                    maxV = k
                else:
                    break
            for j in range(b-1-maxV, b+maxV):
                if switch[j] == 1:
                    switch[j] = 0
                else:
                    switch[j] = 1

# 출력
for i in range(N):
    print(switch[i], end=' ')
    if (i+1) % 20 == 0 and i != 0:
        print()