# 212ms
#https://www.acmicpc.net/problem/5430
# 문제: R과 D로 된 함수목록과 배열을 주고, 배열에 함수목록을 사용하는 법
# 포인트: 리버스를 항상하지 않는다, 에러처리를 한다.
# 힘들었던 부분: []만 들어왔을 경우, ''를 정수로 변환하면서 오류를 처리했었는데,
#              이유는 모르겠지만 []를 pop(), leftpop()에서 오류처리를 하니까 해결됨

import sys
#sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline

TC = int(input())
for tc in range(TC):
    func = input().rstrip() #함수
    N = int(input()) # 배열 길이

    arr = deque(input().rstrip()[1:-1].split(',')) #숫자리스트의 괄호 없애기

    # 빈 리스트가 들어올 경우 ''가 생성되서, 아얘 아무값 안들어올 경우를 따로 적어줌.
    if N == 0:
        arr = deque()
    
    r_count = 0 # reverse가 몇 번 들어왔는지!
    try:
        for active in func: #행동
            if active == 'R':
                r_count += 1
            elif active == 'D':
                if r_count % 2 == 1: # 리버스가 홀수일때 짝수일때 뺴는 위치 바꿔줌
                    arr.pop()
                else:
                    arr.popleft()
    except:
        print('error') #pop or popleft오류
        continue

    if r_count % 2 == 1: #리버스가 홀수면 진짜 뒤집어줌
        arr.reverse()

    print('[', end='')
    print(','.join(arr), end='')
    print(']')








