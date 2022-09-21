N = int(input())
M = int(input())
arr = input()


trg = False   # I를 찾으면, 진행한다.
trg_count = 0 # OI가 몇개 있는지
count = 0     # 총 count
i = 0         # index
while i < M:
    if trg is False:      # I를 찾지못했을 때
        if arr[i] == 'I': # I를 찾으면
            trg = True    # OI를 찾는 것으로 넘어간다.
        i += 1
    if trg is True:           # I를 찾으면
        if arr[i:i+2] == 'OI':# OI를 찾아본다.
            trg_count += 1    # OI개수 세기
            i += 2
        else:
            trg = False      # OI가 아니면 초기화
            trg_count = 0
        
        if trg_count >= N :  # 찾는 길이 (N)이상이면 1씩 더한다.
            count += 1   

print(count)

# 실버1 / 1시간 / 292ms 