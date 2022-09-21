# 실버2 / 328ms
import sys
input = lambda: sys.stdin.readline().strip()

def enq(n):
    global last
    last += 1           # 마지막 정점 추가
    heap[last] = n      # 마지막 정점에 key 추가
    c = last            
    p = c // 2          # 완전이진트리에서 부모 정점 번호

    while p and heap[p] > heap[c]:  # 부모가 있고, 부모 > 자식인 경우 자리 교환
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

def deq(n):
    global last
    tmp = heap[1]                   # 루트 백업
    heap[1] = heap[last]            # 삭제할 노드의 키를 루트에 복사
    if last == 0:
        print(0)
    else:
        last -= 1                                         # 마지막 노드 삭제
        p = 1                                             # 루트에 옮긴 값을 자식과 비교
        c = 2 * p                                         # 왼쪽 자식
        while c <= last:                                  # 자식이 하나라도 있으면
            if c + 1 <= last and heap[c] > heap[c + 1]:   # 오른쪽 자식도 있고, 오른쪽 자식이 더 작으면
                c += 1                                    # 비교 대상을 오른쪽 자식으로 정함
            if heap[p] > heap[c]:                         # 자식이 더 작으면 최소힙 규칙에 어긋나므로
                heap[p], heap[c] = heap[c], heap[p]       # 부모와 자식을 교환
                p = c                                     # 자식을 부모와 교환
                c = p * 2                                 # 왼쪽 자식 번호를 계산
            else:                                         # 부모가 더 작으면
                break                                     # 비교 중단
        print(tmp)


N = int(input())
last = 0
heap = [0] * 100001
for _ in range(N):
    n = int(input())
    if n == 0:
        deq(n)
    else:
        enq(n)