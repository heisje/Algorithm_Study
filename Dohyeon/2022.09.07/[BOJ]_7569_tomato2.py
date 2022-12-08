
import sys
input = sys.stdin.readline
M, N, H = map(int, input().split())

# 거리 탐색으로 풀어보자

tomato = [[[0 for i in range(M)] for j in range(N)] for k in range(H)]