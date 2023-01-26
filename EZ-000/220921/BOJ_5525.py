import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
S = input()

P, i, cnt = 0, 0, 0

while True:
    if M <= i:
        break
    if S[i:i + 3] == 'IOI':
        cnt += 1
        i += 2
        if cnt == N:
            P += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0
    
print(P)

"""참고
https://black-hair.tistory.com/135
"""
