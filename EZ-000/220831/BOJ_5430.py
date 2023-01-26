import sys
input = lambda: sys.stdin.readline().strip()

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    str_arr = input()
    arr = []

    num = ''
    for c in str_arr:
        if 47 < ord(c) < 58:
            num += c
        elif c == ',' or c == ']':
            arr.append(num)
            num = ''

    r = 1
    left = 0
    right = 0
    for func in p:
        if func == 'D':
            if r == 1:
                left += 1
            else:
                right += 1
        else:
            r = -1 if r == 1 else 1
    
    result = 'error' if n < left + right else arr[left:n - right][::r]
    if result != 'error':
        result = '[' + ','.join(result) + ']'
    
    print(result)
