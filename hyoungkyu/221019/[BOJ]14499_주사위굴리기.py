# 골드4 / 72ms
import sys
input = lambda:sys.stdin.readline().strip()

D = [[0, 0], [0, 1], [0, -1], [-1, 0], [1, 0]]              # 동서북남
dic = {'밑':0, '동':0, '서':0, '남':0, '북':0, '위':0}        # 주사위 

def move(x, y, direction):                                  # 주사위 이동 시 행동과 주사위 상태 변화
    if direction == 1:                                      # 동쪽으로 이동
        if arr[x][y] == 0:                                  # 이동 위치의 지도가 0이면
            arr[x][y] = dic['동']                           # 주사위의 숫자를 지도에 복사
        else:                                               # 0이 아니면
            dic['동'] = arr[x][y]                           # 지도의 숫자를 주사위에 복사 후 지도를 0으로
            arr[x][y] = 0
        dic['서'], dic['위'], dic['동'], dic['밑'] = dic['밑'], dic['서'], dic['위'], dic['동'] # 주사위 상태 변화

    elif direction == 2:
        if arr[x][y] == 0:
            arr[x][y] = dic['서']
        else:
            dic['서'] = arr[x][y]
            arr[x][y] = 0
        dic['서'], dic['위'], dic['동'], dic['밑'] = dic['위'], dic['동'], dic['밑'], dic['서']

    elif direction == 3:
        if arr[x][y] == 0:
            arr[x][y] = dic['북']
        else:
            dic['북'] = arr[x][y]
            arr[x][y] = 0
        dic['북'], dic['위'], dic['남'], dic['밑'] = dic['위'], dic['남'], dic['밑'], dic['북']
    
    elif direction == 4:
        if arr[x][y] == 0:
            arr[x][y] = dic['남']
        else:
            dic['남'] = arr[x][y]
            arr[x][y] = 0
        dic['북'], dic['위'], dic['남'], dic['밑'] = dic['밑'], dic['북'], dic['위'], dic['남']
    return dic['위']                                        # 이동 후 주사위 위쪽의 숫자 반환

def f_dice(x, y, direction):                                # 주사위 이동이 유효한지 판단하는 함수
    nx, ny = x + D[direction][0], y + D[direction][1]
    if 0>nx or nx>=N or 0>ny or ny>=M:                      # 이동이 안되면
        return x, y                                         # 원래 위치 반환
    else:
        print(move(nx, ny, direction))                      # 이동이 가능하면 move 함수 실행 후 출력
        return nx, ny                                       # 이동 위치 반환

N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
direction = list(map(int, input().split()))
for i in direction:
    x, y = f_dice(x, y, i)
