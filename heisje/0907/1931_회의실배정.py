import sys
input = lambda:sys.stdin.readline().strip()

N = int(input())
arr = [[]for _ in range(N)]

# 시작이랑 끝점을 튜플로 저장
for n in range(N):
    s, e = map(int, input().split()) 
    arr[n] = (s, e)
arr.sort()

ed = 0    # end 앞의 회의가 끝난지점
count = 0 # 개수세기
for a in arr:
    if a[0] >= ed: # 시작점이 end(앞의 회의가 끝난시점)보다 크면
        ed = a[1]  # 회의를 넣고
        count += 1 # 회의 개수를 늘린다.
    elif a[1] <= ed: # 시작점이 end(앞의 회의가 끝난시점)보다 작은 대신, 끝이 빠르면 교체해서 넣기
        ed = a[1]
print(count) #개수 세기

#실버 1 / 284ms or 4280ms / 50분

