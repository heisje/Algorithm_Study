# 실버1 / 668ms
import sys
input = lambda:sys.stdin.readline().strip()

# BFS
N, K = map(int, input().split())
if N >= K:                              # 수빈이가 동생보다 오른쪽인 경우 -> 텔포 X
    print(abs(K-N))
else:                                   # 왼쪽인 경우
    lst = [100000] * (2*K+1)            # 초기값 100000을 갖는 2K+1 개의 리스트 생성
    queue = []
    queue.append(N)                     # 초기 위치 추가
    lst[N] = 0                          # 초기 위치 설정
    tmp = []                            # 한 큐가 다 돌면 큐를 채워줄 용도
    cnt = 1                             # 시간 변수
    while queue:
        t = queue.pop(0)
        if t == K:                      # 목표값 도달 시 break
            break
        if 0<=t-1 and cnt < lst[t-1]:   # 왼쪽으로 한칸
            lst[t-1] = cnt
            tmp.append(t-1)
        if t+1<2*K and cnt < lst[t+1]:  # 오른쪽으로 한칸
            lst[t+1] = cnt
            tmp.append(t+1)
        if t <= K and cnt < lst[2*t]:   # 텔레포트
            lst[2*t] = cnt
            tmp.append(2*t)
        if queue == []:                 # 한 큐가 다 돌면
            queue = tmp[:]              # 큐를 다시 리필
            cnt += 1                    # 한 큐가 끝났으니 시간 변수(cnt) +1 해줌
            tmp = []                    # 다음 큐를 받기 위해 초기화
    print(lst[K])