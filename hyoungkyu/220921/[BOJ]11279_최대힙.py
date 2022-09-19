# 실버2 / 332ms
import sys
input = lambda:sys.stdin.readline().strip()

# 최대힙 원소 넣기
def enq(n):
    global last
    last += 1               # 마지막 정점 추가
    heap[last] = n          # 마지막 정점에 key 추가
    c = last                # 마지막 정점 번호
    p = c // 2              # 완전이진트리에서 부모 정점 번호

    # 부모가 있고, 부모 < 자식인 경우 자리 교환
    while p and heap[c] > heap[p]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

# 최대힙의 루트 출력
def deq():
    global last
    if last == 0:                                       # heap이 비어있으면
        return 0                                        # 0 반환
    else:                                               # heap이 비어있지 않으면
        tmp = heap[1]                                   # 루트 백업
        heap[1] = heap[last]                            # 삭제할 노드의 키를 루트에 복사
        last -= 1                                       # 마지막 노드 삭제
        p = 1                                           # 루트에 옮긴 값을 자식과 비교
        c = 2 * p                                       # 왼쪽 자식과 비교
        while c <= last:                                # 자식이 하나라도 있으면
            if c+1 <= last and heap[c] < heap[c+1]:     # 오른쪽 자식이 왼쪽 자식보다 크면
                c += 1                                  # 비교 대상을 오른쪽 자식으로 정함
            if heap[p] < heap[c]:                       # 자식이 부모보다 크면
                heap[p], heap[c] = heap[c], heap[p]     # 교환
                p = c                                   # 자식을 새로운 부모로
                c = p * 2                               # 왼쪽 자식 번호를 계산
            else:                                       # 부모가 더 크면
                break                                   # 비교 중단
        return tmp                                      # 백업한 최대값 반환

E = int(input())
heap = [0] * (E+1)
last = 0
for _ in range(E):
    n = int(input())
    if n == 0:
        print(deq())
    else:
        enq(n)