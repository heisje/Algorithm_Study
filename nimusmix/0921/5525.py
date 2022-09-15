import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())
M = int(input())
S = input()
word = 'I' + 'OI' * N
cnt = 0

for i in range(M):
    if S[i:i+(N*2+1)] == word:
        cnt += 1

print(cnt)