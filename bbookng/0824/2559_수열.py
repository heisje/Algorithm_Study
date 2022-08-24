import sys
input = lambda : sys.stdin.readline().strip()

N, K = map(int, input().split())
arr = list(map(int, input().split()))


tmp = sum(arr[0:K])                 # 첫번째 부터 K 번까지
board = [tmp]                       # 수열 담기

for i in range(N-K):
    tmp = tmp - arr[i] + arr[i+K]   # 왼쪽 빼고 오른쪽 더하고
    board.append(tmp)

print(max(board))                   # 최댓값 찾기