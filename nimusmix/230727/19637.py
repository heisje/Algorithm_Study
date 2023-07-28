import sys
input = sys.stdin.readline

def binary_search(person, info):
    l, r = 0, N - 1
    
    while l <= r:
        m = (l + r) // 2
        
        if person <= int(info[m][1]):
            r = m - 1
        else:
            l = m + 1
            
    return info[r+1][0]


N, M = map(int, input().split())
info = [input().split() for _ in range(N)]

for _ in range(M):
    print(binary_search(int(input()), info))