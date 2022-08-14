#문제: 개미가 한방향으로 쭉 움직였을때, 좌표를 구하라. 단 개미는 edge를 만나면 반사회전한다.

#풀이법: 1번 반사되면 -1을 곱한거와 같아지고, 2번 반사되면 원래대로 돌아가는 것을 사용

W, H = map(int, input().split()) #그리드 W H
x, y = map(int, input().split()) #개미위치 X Y
HOUR = int(input())              #시간 HOUR

def check(x, W):
    if ((x + HOUR) // W) % 2 == 0: # x + HOUR가 w로 나누었을 때 짝수면!
        return (x + HOUR) % W      # 똑같이 나온다
    else:
        return (W - (x + HOUR) % W) # 아닐 시엔 뒤집혀서 나온다
print(check(x, W), check(y,H))