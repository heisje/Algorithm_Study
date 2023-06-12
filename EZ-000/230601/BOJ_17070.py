import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
wall = [list(map(int, input().split())) for _ in range(N)]
que = deque([(0, 1, 0)])
visited = {(0, 1, 0)}
dr = (0, 1, 1)
dc = (1, 0, 1)
