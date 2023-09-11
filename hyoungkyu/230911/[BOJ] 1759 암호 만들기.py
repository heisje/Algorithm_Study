# 골드5 / 56ms
L, C = map(int, input().split())

lst = list(input().split())
lst.sort()

def solution(s, idx):
    if len(s) == L:
        if is_possible(s):
            print(s)
        return

    for i in range(idx, C):
        solution(s+lst[i], i+1)

def fn(char):
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        return True
    return False

def is_possible(s):
    flag1 = False
    flag2 = False
    cnt = 0
    for char in s:
        tmp = fn(char)
        if tmp:
            flag1 = True
        else:
            cnt += 1
            if cnt >= 2:
                flag2 = True
    return True if flag1 and flag2 else False


solution('', 0)