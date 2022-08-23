import sys
input = sys.stdin.readline


def min_d(w, h, n, arr):
    # loca 안 만들어도 가능 ..
    loca = []
    for lst in arr:
        if lst[0] == 1:
            loca.append((0, lst[1]))
        elif lst[0] == 2:
            loca.append((h, lst[1]))
        elif lst[0] == 3:
            loca.append((lst[1], 0))
        else:
            loca.append((lst[1], w))

    d_sum = 0
    for idx in range(n):
        temp = 0
        # 동근이랑 상점이 같은 선 위에 있을 때
        if arr[-1][0] == arr[idx][0]:
            a = loca[-1][0] - loca[idx][0]
            b = loca[-1][1] - loca[idx][1]
            temp = a if a != 0 else b
            temp = -temp if temp < 0 else temp
        # 동근이가 북쪽(1)에 있을 때
        elif arr[-1][0] == 1:
            if arr[idx][0] == 3:
                temp = loca[-1][1] + loca[idx][0]
            elif arr[idx][0] == 4:
                temp = w - loca[-1][1] + loca[idx][0]
            else:
                temp = min(loca[-1][1] + loca[idx][1] + h, w - loca[-1][1] + w - loca[idx][1] + h)
        # 동근이가 남쪽(2)에 있을 때
        elif arr[-1][0] == 2:
            if arr[idx][0] == 3:
                temp = loca[-1][1] + h - loca[idx][0]
            elif arr[idx][0] == 4:
                temp = w - loca[-1][1] + h - loca[idx][0]
            else:
                temp = min(loca[-1][1] + loca[idx][1] + h, w - loca[-1][1] + w - loca[idx][1] + h)
        # 동근이가 서쪽(3)에 있을 때
        elif arr[-1][0] == 3:
            if arr[idx][0] == 1:
                temp = loca[-1][0] + loca[idx][1]
            elif arr[idx][0] == 2:
                temp = h - loca[-1][0] + loca[idx][1]
            else:
                temp = min(loca[-1][0] + loca[idx][0] + w, h - loca[-1][0] + h - loca[idx][0] + w)
        # 동근이가 동쪽(4)에 있을 때
        elif arr[-1][0] == 4:
            if arr[idx][0] == 1:
                temp = loca[-1][0] + w - loca[idx][1]
            elif arr[idx][0] == 2:
                temp = h - loca[-1][0] + w - loca[idx][1]
            else:
                temp = min(loca[-1][0] + loca[idx][0] + w, h - loca[-1][0] + h - loca[idx][0] + w)
        # 상점과 동근이의 위치에 맞는 거리 값 temp를 전체 거리 합 d_sum에 더하기
        d_sum += temp

    return d_sum


W, H = map(int, input().split())
N = int(input())
locations = []
for _ in range(N + 1):
    locations.append(list(map(int, input().split())))
print(min_d(W, H, N, locations))


'''
참고: https://ji-gwang.tistory.com/m/326
'''
