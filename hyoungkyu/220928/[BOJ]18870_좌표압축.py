# 실버2 / 6280ms 
import sys
input = lambda:sys.stdin.readline().strip()

def bin_search(s, e, n):
    global tmp
    m = (s + e) // 2
    if n == Y[m]:
        tmp = m
        return
    if n < Y[m]:
        e = m - 1
        bin_search(s, e, n)
    elif n > Y[m]:
        s = m + 1
        bin_search(s, e, n)
    else:
        tmp = 0
        return 

N = int(input())
X = list(map(int, input().split()))         # 입력 리스트
Y = sorted(set(X))                          # 중복 제거 & 정렬 리스트
dic = {}                                    # Memoization
for i in range(N):                          # 입력 리스트 전체 순회
    if X[i] in dic:                         # 이전에 구해놨으면 continue
        continue
    tmp = 0                                 # 이진탐색으로 구할 개수 변수
    bin_search(0, len(Y)-1, X[i])           # 이진탐색
    dic[X[i]] = tmp                         # 이진탐색으로 구한 개수를 dic에 저장

for i in X:                                 # 출력
    print(dic[i], end=' ')