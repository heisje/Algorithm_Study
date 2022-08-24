import sys
sys.stdin = open('input.txt')
# 푸는 방법: 거리를 구해야하는데,
# 원의 거리에서 한 방향으로 돌았을 때 거리와, 반대방향으로 갔을때의 거리중 짧은 것을 다 더한다.
# 이때, 원의 둘레에서 한 방향으로 갔을때를 빼면 반대방향이 나오는 것을 이용한다.
# 1 = 북쪽
# 2 = 남쪽
# 3 = 서쪽
# 4 = 동쪽

#입력
W, H = map(int, input().split()) # 맵의 크기
N = int(input())
arr = [] #배열
for n in range(N): # 상점 거리 개수
    arr.append(list(map(int, input().split()))) #상점 입력
st, st_w = map(int, input().split())            #동근(시작) 위치


# 시계방향으로 보았을 때 기준점으로 변환 ( 남과 서가 바뀐다. )
for a in range(len(arr)):
    if arr[a][0] == 2:  #남쪽일 경우
        arr[a][1] = W - arr[a][1]
    elif arr[a][0] == 3: #서쪽일 경우
        arr[a][1] = H - arr[a][1]
if st == 2: st_w = W - st_w #시작지점도 마찬가지
elif st == 3: st_w = H - st_w

#print(arr, st, st_w)

#탐색 전 세팅
rotate = [1, 4, 2, 3] #북 동 남 서 시계방향
a = rotate.index(st) # 시작할 인덱스 탐색, for안의 turn에서 더해지면서 찾는다.
#탐색
result = []
for find in arr: #모든 정답 찾기

    #시작점을 세팅하고
    if st in [1, 2]:
        gap = W - st_w
    else:
        gap = H - st_w

    #탐색
    for turn in range(1, 5): #한방향으로 돌면서 찾기
        view = rotate[(a + turn) % 4] #다음으로 쳐다볼 방향
        if view == find[0]: #쳐다볼 방향과 같으면
            gap += find[1]
            break
        else:                       #다른 방향이면
            if view in [1, 2]: #북, 남이면
                gap += W
            else: #서, 동이면
                gap += H

    #다른 방향이 더 가까울지도 탐색
    if gap > 2 * (W + H) - gap:
        gap = abs(2 * (W + H) - gap)
    result.append(gap)
print(sum(result))
