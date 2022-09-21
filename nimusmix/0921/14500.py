from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()

def first(i, j):
    first = first2 = 0
    for n in range(4):
        if j+4 <= M:
            first += paper[i][j+n]
        if i+4 <= N:
            first2 += paper[i+n][j]
    return max(first, first2)

def second(i, j):
    second = second2 = second3 = second4 = second5 = second6 = second7 = second8 = 0
    for n in range(3):
        if j+3 <= M:
            second2 += paper[i][j+n]
            second4 += paper[i][j+n]
            second6 += paper[i][j+n]
            second8 += paper[i][j+n]
        if i+3 <= N:
            second += paper[i+n][j]
            second5 += paper[i+n][j]
            second7 += paper[i+n][j]
            if j+1 < M:
                second3 += paper[i+n][j+1]
                
    if i+2 < N and j+1 < M:
        second += paper[i+2][j+1]
    if 0 <= i-1:
        second6 += paper[i-1][j]
        if j+2 < M:
            second2 += paper[i-1][j+2]
    second3 += paper[i][j]
    if i+1 < N:
        second4 += paper[i+1][j]
        if j+2 < M:
            second8 += paper[i+1][j+2]
    if i+2 < N and 0 <= j-1:
        second5 += paper[i+2][j-1]
    if j+1 < M:
        second7 += paper[i][j+1]

    return max(second, second2, second3, second4, second5, second6, second7, second8)

def third(i, j):
    third = third2 = third3 = third4 = 0
    for n in range(2):
        if i+3 <= N:
            if j+1 < M:
                third += paper[i+n][j]
                third += paper[i+n+1][j+1]
            if 0 <= j-1:
                third3 += paper[i+n][j]
                third3 += paper[i+n+1][j-1]
        if j+3 <= M:
            if 0 <= i-1:
                third2 += paper[i][j+n]
                third2 += paper[i-1][j+n+1]
            if i+1 < N:
                third4 += paper[i][j+n]
                third4 += paper[i+1][j+n+1]
    return max(third, third2, third3 ,third4)
    
def fourth(i, j):
    fourth = fourth2 = fourth3 = fourth4 = 0
    for n in range(3):
        if j+3 <= M:
            fourth += paper[i][j+n]
            fourth3 += paper[i][j+n]
        if i+3 <= N:
            fourth2 += paper[i+n][j]
            fourth4 += paper[i+n][j]
    
    if i+1 < N and j+1 < M:
        fourth += paper[i+1][j+1]
        fourth2 += paper[i+1][j+1]
    if 0 <= i-1 and j+1 < M:
        fourth3 += paper[i-1][j+1]
    if i+1 < N and 0 <= j-1:
        fourth4 += paper[i+1][j-1]
    return max(fourth, fourth2, fourth3, fourth4)

def fifth(i, j):
    fifth = 0
    if j+1 < M and i+1 < N:
        fifth += paper[i][j]
        fifth += paper[i+1][j]
        fifth += paper[i][j+1]
        fifth += paper[i+1][j+1]
    return fifth

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
values = deque()

for i in range(N):
    for j in range(M):
            values.append(max(first(i, j), second(i, j), third(i, j), fourth(i, j), fifth(i, j)))

print(max(values))