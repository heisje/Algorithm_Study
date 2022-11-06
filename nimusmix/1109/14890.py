import sys
input = lambda: sys.stdin.readline().strip()

N, L = map(int, input().split())
map1 = [tuple(map(int, input().split())) for _ in range(N)]
map2 = list(zip(*map1))
cnt = 0

def sol(road):
    global cnt
    
    if len(set(road)) == 1:                                       # 모든 칸의 높이가 같으면 cnt += 1
        cnt += 1
        return
    
    for i in range(N-1):
        high = i if road[i] > road[i+1] else (i + 1)              # 현재 칸과 다음 칸 중에 높은 칸
        low = (i + 1) if road[i] > road[i+1] else i               # 현재 칸과 다음 칸 중에 낮은 칸
        LEN = L if road[i] > road[i+1] else -L                    # i가 더 높으면 +L, i+1이 더 높으면 -L을 인덱스에 더해서 비교하기 위함.
        
        if road[high] == road[low]:                               # 두 칸의 높이가 같으면 continue
            continue
        
        if road[high] - road[low] > 1:                            # 두 칸의 높이가 1 이상 차이나면 return
            return
        
        if 0 <= high + LEN < N:                                   # 다리를 놓았을 때 길 안에 위치해야 함.
            if 0 < LEN:                                           # LEN이 0보다 클 때 (i가 i+1보다 클 때)
                if len(set(road[high:high+LEN+1])) > 2:           # 다리를 놓는 범위 내에 다른 길이가 2개 이상 있으면 return
                    return                                        # (높은 높이, 낮은 높이 둘만 있어야 함.)
                    
                for j in range(high+1, high+(2*LEN)+1):           # 다리를 놓았을 때 반대편에서 같은 범위에 다리가 또 놓이면 안 되므로,
                    if j < N and road[j] >= road[high]:           # low부터 (high + 2*LEN)의 범위까지는 road[high]보다 항상 낮아야 함.
                        return
            else:                                                 # LEN이 0보다 작을 때 (i+1이 i보다 클 때)
                if len(set(road[high+LEN:high+1])) > 2:           # 다리를 놓는 범위 내에 다른 길이가 2개 이상 있으면 return
                    return                                        # (높은 높이, 낮은 높이 둘만 있어야 함.)
                    
                for j in range(high+(2*LEN), high):               # 다리를 놓았을 때 반대편에서 같은 범위에 다리가 또 놓이면 안 되므로,
                    if 0 <= j and road[j] >= road[high]:          # low부터 (high + 2*LEN)의 범위까지는 road[high]보다 항상 낮아야 함.
                        return
        else:
            return
    cnt += 1

for m in map1:
    sol(m)
    
for m in map2:
    sol(m)

print(cnt)