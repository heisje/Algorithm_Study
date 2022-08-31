N, r, c = map(int, input().split())
order = 0

for n in range(N - 1, -1, -1):
    # l = 4분면 각 변의 길이 length
    l = 2 ** n
    
    # 2사분면
    if r < l and c >= l:
        order += 2 ** (n + n)
        c -= l

    # 3사분면
    elif r >= l and c < l:
        order += 2 * (2 ** (n + n))
        r -= l
    
    # 4사분면
    elif r >= l and c >= l:
        order += 3 * (2 ** (n + n))
        r -= l
        c -= l

print(order)

'''참고
https://ggasoon2.tistory.com/11
'''
