import sys
input = lambda :sys.stdin.readline().strip()

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

arr.sort(key= lambda x:x[0])            # 시작시간, 끝나는시간 둘 다 오름차순으로 정렬
arr.sort(key= lambda x:x[1])

tmp = 0                                 # 끝나는 시간
cnt = 0                                 # 회의 개수

for s, e in arr:
    if s >= tmp:                        # 시작 시간이 끝나는 시간보다 크다면 
        cnt += 1                        # 사용할 수 있는 회의 하나 추가
        tmp = e                         # 끝나는 시간 갱신

print(cnt)