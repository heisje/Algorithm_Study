import sys, heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    visited = [0] * 1000001
    Q1 = []                                             # 최소힙
    Q2 = []                                             # 최대힙

    for i in range(K):
        a, b = input().split()
        b = int(b)
        if a == 'I':                                    # I 면 push, i 로 index 표시
            heapq.heappush(Q1, (b, i))
            heapq.heappush(Q2, (-b, i))                 # '-' 붙여서 넣어 최대 힙 구현
        else:
            if b == 1:                                  # 1이면
                while Q2 and visited[Q2[0][1]] == 1:    # 방문했던 곳이면 Q1에서 pop 됐다는 거니까
                   heapq.heappop(Q2)                    # 없애주기
                if Q2:                                  # Q2가 없을때 pop 하면 에러 나니까 있을 때
                    visited[Q2[0][1]] = 1               # 방문표시
                    heapq.heappop(Q2)                   # pop
            if b == -1:                                 # 위와 같은 로직으로 최솟값 삭제 과정
                while Q1 and visited[Q1[0][1]] == 1:
                    heapq.heappop(Q1)
                if Q1:
                    visited[Q1[0][1]] = 1
                    heapq.heappop(Q1)
    print(Q1, Q2)

    while Q1 and visited[Q1[0][1]] == 1:                # 방문했는데 미처 삭제되지 못한거 다 빼주기
        heapq.heappop(Q1)
    while Q2 and visited[Q2[0][1]] == 1:
        heapq.heappop(Q2)

    print(Q1, Q2)

    if not Q1:                                          # 비어있으면
        print('EMPTY')
    else:                                               # 최대, 최소값 출력
        print(-Q2[0][0], Q1[0][0])                      # 최대힙 음수로 저장돼있으니 - 붙여서 나오기

