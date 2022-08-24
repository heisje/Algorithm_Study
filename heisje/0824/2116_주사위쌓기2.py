import sys
sys.stdin = open('input.txt')
#문제를 잘읽자!
#모든 경우의 수는 6개......

def sol(N):
    result = []
    
    #맨 윗면 주사위 돌리기의 가짓수
    for top_idx in range(6): # top_idx  # 윗면의 숫자를 가진 arr속의 index
        sum_r = side(top_idx, arr[0]) #합계저장
        top = arr[0][top_idx]         # top = 윗면의 숫자

        #그 밑의 주사위 쌓기
        for n in range(1, N):             #주사위를 차례로 쌓기
            top_idx = arr[n].index(top)   #맨 윗면의 인덱스를 구해주기
            top = arr[n][top_bo(top_idx)] #구한 인덱스로 윗면의 숫자를 바꿔줌
            sum_r += side(top_idx, arr[n])#윗면과 아랫면을 제외한 최대값을 구해줌
        result.append(sum_r)#더한 값 저장
    return max(result) #더한 값 중 최대값 저장

def top_bo(t): #인덱스를 넣으면 반대위치 인덱스를 return해주는 함수
    if t == 0: return 5
    if t == 5: return 0
    if t == 1: return 3
    if t == 3: return 1
    if t == 2: return 4
    if t == 4: return 2
def side(t, li): #인덱스를 넣으면 맥스값을 리턴
    if t == 0: return max(li[1],li[2],li[3],li[4])
    if t == 5: return max(li[1],li[2],li[3],li[4])
    if t == 1: return max(li[0],li[2],li[5],li[4])
    if t == 3: return max(li[0],li[2],li[5],li[4])
    if t == 2: return max(li[1],li[0],li[3],li[5])
    if t == 4: return max(li[1],li[0],li[3],li[5])

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
print(sol(N))
