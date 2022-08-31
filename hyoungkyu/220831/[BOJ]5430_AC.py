# ms / 골드5
import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

# R : 수의 순서를 뒤집는 함수, D : 첫번째 수를 버리는 함수
# 문자로 받아서 양옆 []을 없애고 데크에 담아서 함수에 따라 진행
T = int(input())
for _ in range(T):
    p = deque(input())
    n = int(input())
    tmp = input().lstrip('[').rstrip(']')
    if tmp == '':
        arr = deque()
    else:
        arr = deque(map(int, tmp.split(',')))
    K = 0                                       # R에 따라 앞 or 뒤를 나타내는 변수
    cnt = 0                                     # R의 개수를 세는 변수
    try:
        for i in p:
            if i == 'R':
                cnt += 1
                if K == 0:
                    K = -1
                else:
                    K = 0
            elif i == 'D':
                if K == 0:
                    arr.popleft()
                else:
                    arr.pop()
        else:
            s = ''
            if cnt % 2 == 0:
                for j in range(len(arr)):
                    if j == len(arr)-1:
                        s += str(arr[j])
                    else:
                        s += str(arr[j]) + ','
            else:
                for j in range(len(arr)-1, -1, -1):
                    if j == 0:
                        s += str(arr[j])
                    else:
                        s += str(arr[j]) + ','
            s = '[' + s + ']'
            print(s)

    except:
        print('error')
