N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

def first(i, j):
    first = 0
    for n in range(4):
        first += paper[i][j+n]
    return first

def first2(i, j):
    first2 = 0
    for n in range(4):
        first2 += paper[i+n][j]
    return first2

def second(i, j):
    second = 0
    for n in range(3):
        second += paper[i+n][j]
    second += paper[i+2][j+1]
    return second

def third(i, j):
    third = 0
    for n in range(2):
        third += paper[i+n][j]
    for n in range(1, 3):
        third += paper[i+n][j+1]
    return third
    
def fourth(i, j):
    fourth = 0
    for n in range(3):
        fourth += paper[i][j+n]
    fourth += paper[i+1][j+1]
    return fourth

def fifth(i, j):
    fifth = 0
    for n in range(2):
        fifth += paper[i][j+1]
        fifth += paper[i+1][j]
    return fifth

