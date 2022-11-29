# 골드5 / 84ms
import sys
from collections import deque
input = lambda:sys.stdin.readline().strip()

# 톱니바퀴의 정보, N : 0, S : 1, (12시부터 시계방향)
Tooths = [deque(map(int, input())) for _ in range(4)]                

K = int(input())

# 회전 정보, 0 : 톱니바퀴 번호, 1 : 방향 (1 : 시계, -1 : 반시계)
Rotations = [list(map(int, input().split())) for _ in range(K)]

def rot(idx, dir):                                              # 회전 함수
    if dir == 1:                                                # 다른 톱니바퀴가 움직이는 방향이 시계일 때
        tmp = Tooths[idx].popleft()
        Tooths[idx].append(tmp)
        dir = -1
    else:                                                       # 다른 톱니바퀴가 움직이는 방향이 반시계일 때
        tmp = Tooths[idx].pop()
        Tooths[idx].appendleft(tmp)
        dir = 1
    return dir


def chain(idx, dir):                                            # 하나를 돌릴 때 연쇄적으로 돌아가는 함수
    idx -= 1                                                    # 인덱스 맞추기
    l = 0                                                       # 왼쪽에 연결된 톱니의 개수
    r = 0                                                       # 오른쪽에 연결된 톱니의 개수
    dir_l = dir
    dir_r = dir
    while True:                                                 # 각 방향별 연결된 톱니의 개수 구하기
        if 0 <= idx-l-1 and Tooths[idx-l-1][2] != Tooths[idx-l][6]:
            l += 1
        elif idx+r+1 < 4 and Tooths[idx+r][2] != Tooths[idx+r+1][6]:
            r += 1
        else:
            break
    # print(l, r)
    # 톱니 돌리기 (-dir인 이유는 얘는 누가 돌려주는게 아니라 자기가 돌아가므로 -dir이 원래 자기가 돌아가는 방향)
    rot(idx, -dir)                                              
    for i in range(l):                                          # 왼쪽 돌리기
        dir_l = rot(idx-i-1, dir_l)
    for i in range(r):                                          # 오른쪽 돌리기
        dir_r = rot(idx+i+1, dir_r)

for idx, dir in Rotations:                                      # K번 돌리기 ㄱㄱ
    chain(idx, dir)

tot = 0                                                         # 점수 구하기
for i in range(4):
    if Tooths[i][0]:
        tot += 2**(i)
print(tot)

