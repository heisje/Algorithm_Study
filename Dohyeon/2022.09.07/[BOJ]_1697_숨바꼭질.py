import sys
from collections import deque

input = sys.stdin.readline
subin, bro = map(int,input().split())


def BFS(start, target):
    queue = deque([start])
    distance = [0]*100001 # distance로 방문 여부와 소요 시간을 함께 저장 인덱스 에러 방지 +1 만큼 더 만듦

    while queue :
        node = queue.popleft()
        for next in [node-1, node+1, node*2] :
            if next < 0 or next > 100000:
                continue
            if distance[next]:
                continue
            if next == target :
                return distance[node] + 1
            if 0 <= next <= 100000 :
                queue.append(next)
                distance[next] = distance[node] + 1

if subin == bro:
    print(0)
else :
    print(BFS(subin,bro))