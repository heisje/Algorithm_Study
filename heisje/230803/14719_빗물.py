# 72ms

def main():
    # 맥스치를 저장해둔다
    # 맥스치 기준으로 바깥에서 들어오며 비의 량을 찾는다.
    answer = 0
    maxValue = 0
    maxIdx = 0
    for idx, value in enumerate(ground):
        if value > maxValue:
            maxValue = value
            maxIdx = idx
    
    left_max = 0
    for i in range(0, maxIdx):
        if left_max < ground[i]:
            left_max = ground[i]
        else:
            answer += left_max - ground[i]

    right_max = 0
    for i in range(len(ground)-1, maxIdx, -1):
        if right_max < ground[i]:
            right_max = ground[i]
        else:
            answer += right_max - ground[i]

    print(answer)

H, W = input().split()
ground = list(map(int, input().split()))
main()