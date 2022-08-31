from collections import deque

N, M = map(int, input().split()) #N은 포인트 개수, M은 노드갯수
arr = [[] for _ in range(N+1)]
for _ in range(M): #노드입력
    F, T = map(int, input().split())
    arr[F].append(T)
    arr[T].append(F)
result = []
for n in range(1, N+1): #모든 케빈베이컨을 구한다. 
    kb = [0] * (N + 1)  #visited
    queue = deque()
    queue.append(n)
    while queue:
        p = queue.popleft()
        for node in arr[p]: #노드들을 다 더한다.
            if kb[node] == 0:
                queue.append(node)
                kb[node] = kb[p] + 1

    result.append((n, sum(kb)-kb[n])) #결과값을 튜플로 저장
print(min(result, key=lambda a:a[1])[0]) #튜플속 [1]에서 min값 구하기





