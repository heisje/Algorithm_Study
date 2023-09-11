# 40ms

# 모음 한개 이상, 최소 두개의 자음

def loop(l, c, ja, mo, result):
    #print(result)
    
    if L - l > C - c:
        # 그냥 끝나버림
        # print('end')
        return
    if l == L:
        # 다 채워짐
        if ja >= 2 and mo >= 1:
            print(''.join(list(map(chr, result))))
        return 
    
    if li[c] in MO:
        # 선택
        loop(l+1, c+1, ja, mo+1, result+[li[c]])
        # 안선택
        loop(l, c+1, ja, mo, result)
    else:
        # 선택
        loop(l+1, c+1, ja+1, mo, result+[li[c]])
        # 안선택
        loop(l, c+1, ja, mo, result)

# L개의 암호, C개의 문자
L, C = map(int, input().split())
li = list(map(ord, input().split()))

# 최소 한 개의 모음 aeiou
MO = set([97, 101, 105, 111, 117])
answer = []

# 순서대로
li.sort()

loop(0, 0, 0, 0, [])
