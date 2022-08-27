from collections import deque

T = int(input())

for _ in range(T):
    p = deque(input())
    n = int(input())
    digits = input().strip('[')
    
    if digits != ']': 
        digits = deque(map(int, digits.strip(']').split(',')))
    else:
        digits = deque([])
        
    r_cnt = 0
    flag = 1

    for i in p:
        if i == 'R': r_cnt += 1
        else:
            if len(digits) == 0: flag = 0
            elif r_cnt % 2 == 1: digits.pop()
            else: digits.popleft()
    
    if r_cnt % 2 == 1: digits.reverse()

    print('['+','.join(map(str, digits))+']' if flag else 'error')