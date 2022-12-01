# nCn//2
import sys
input = lambda:sys.stdin.readline()

def combination(n, in_com_count,com_A):
    global result
    if in_com_count == N//2:
        com_B = list(set(range(0,N)) - set(com_A))
        team_A = 0
        team_B = 0
        # A와 B의 결과값을 누적한다.
        for main_idx in range(N//2):
            for sub_idx in range(N//2):
                if main_idx < sub_idx:
                    team_A += (arr[com_A[main_idx]][com_A[sub_idx]] + arr[com_A[sub_idx]][com_A[main_idx]])
                    team_B += (arr[com_B[main_idx]][com_B[sub_idx]] + arr[com_B[sub_idx]][com_B[main_idx]])
                    pass
        # 최대값을 찾는다
        if result > abs(team_A - team_B):
            result = abs(team_A - team_B)
        return
    if n == N:
        return
    # 조합을 전부 구한다
    combination(n + 1, in_com_count + 1,com_A + [n])
    combination(n + 1, in_com_count,com_A)

N = int(input())
arr = list(list(map(int, input().split())) for _ in range(N))
visited = [0]*(N//2)
result = 1000000000
combination(0,0,[])
print(result)

# 실버2 / 35분 / 4676ms