from collections import deque


def hide_n_seek(n, k):
    node = deque([n])
    visited = [0] * 100001
    while node:
        now = node.popleft()
        if now == k:
            return visited[now]
        else:
            for new in [now - 1, now + 1, 2 * now]:
                if 0 <= new <= 100000 and not visited[new]:     # 가능한 위치 값이고 visited가 0이면(= 방문 안 했으면)
                    node.append(new)                                # 현재 노드 now에서 파생된 new를 node에 추가
                    visited[new] = visited[now] + 1                 # visited의 new 자리에 깊이 값(=현재 깊이 + 1)을 저장


N, K = map(int, input().split())
print(hide_n_seek(N, K))

'''mini_log
1. deque를 안 쓰고 그냥 리스트와 pop(0)를 쓰니까 시간이 3배 정도 길어짐
    -> deque가 효율적
2. 처음에 visited를 안 쓰고 완전탐색 했을 땐 시간초과
    -> bfs를 효율적으로 사용하기 위해서 이미 간 노드는 확인하지 않기
3. dict로 visited 기록하니 메모리 초과
    -> dict 자료구조는 메모리를 많이 차지
'''
