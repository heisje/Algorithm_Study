
def solution(n, k):
    answer = -1
    if k != 10:
        change_num = ''
        while n:
            change_num += str(n%k)
            n //= k
        s = ''
        for i in change_num:
            s = i + s
    else:
        s = str(n)
    
    # print(f's : {s}')
    
    def f(s):
        num = int(s)
        for i in range(2, int(num**0.5)+1):    # 2인 경우도 포함시키기 위해 +2를 해줌
            if num % i == 0:
                break
        else:
            return 1
        return 0
    
    tmp = ''
    cnt = 0
    check = []
    for i in range(len(s)):
        if 0 < int(s[i]) < 10:
            tmp += s[i]
        else:
            if tmp and tmp != '1':
                if tmp in check:
                    cnt += 1
                elif f(tmp):
                    cnt += 1
                    check.append(tmp)
                # print(f'count : {tmp}')
            tmp = ''
    
    if tmp and tmp != '1':
        if tmp in check or f(tmp):
            cnt += 1
        # print(f'count : {tmp}')
            
    answer = cnt
    return answer

'''
테스트 1 〉통과 (94.32ms, 10.3MB)
테스트 2 〉통과 (0.03ms, 10.4MB)
테스트 3 〉통과 (0.04ms, 10.5MB)
테스트 4 〉통과 (0.04ms, 10.4MB)
테스트 5 〉통과 (0.09ms, 10.4MB)
테스트 6 〉통과 (0.05ms, 10.5MB)
테스트 7 〉통과 (0.03ms, 10.5MB)
테스트 8 〉통과 (0.06ms, 10.3MB)
테스트 9 〉통과 (0.05ms, 10.4MB)
테스트 10 〉통과 (0.08ms, 10.5MB)
테스트 11 〉통과 (0.05ms, 10.4MB)
테스트 12 〉통과 (0.04ms, 10.4MB)
테스트 13 〉통과 (0.05ms, 10.2MB)
테스트 14 〉통과 (0.03ms, 10.4MB)
테스트 15 〉통과 (0.03ms, 10.4MB)
테스트 16 〉통과 (0.03ms, 10.4MB)
'''