import sys

input = lambda: sys.stdin.readline().strip()
N = int(input())

def func(A, B, k=4):  # 재귀함수 만들기
    if k == 0:
        print('D')
        return

    if A.count(k) > B.count(k):
        print('A')
        
    elif A.count(k) < B.count(k):
        print('B')
       
    else:
        k -= 1
        func(A, B, k)

i = 1
while i <= N:
    A = list(map(int, input().split()))
    B = list(map(int,input().split()))
    a = A.pop(0)
    b = B.pop(0)
    func(A, B)
    i += 1