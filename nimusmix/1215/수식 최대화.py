from itertools import permutations

def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiple(x, y):
    return x * y

def solution(expression):
    ans, arr, pre = [], [], 0
    
    for idx, i in enumerate(expression):                                                  # expression을 숫자와 연산자로 분리하여 arr에 저장
        if not i.isdigit():
            arr.append(int(expression[pre:idx]))
            arr.append('plus' if i == '+' else 'minus' if i == '-' else 'multiple')
            pre = idx + 1
    arr.append(int(expression[pre:]))                                                     # 마지막 연산자까지 더해지고 for문이 종료되므로 마지막 숫자까지 저장
    
    OP = ['plus', 'minus', 'multiple']
    for operators in permutations(OP, 3):                                                 # 모든 연산자 우선순위 경우의 수
        tmp = arr[:]
        for operator in operators:                                                        # 순서대로 순회하며
            idx = 1
            while idx < len(tmp):
                if tmp[idx] == operator:                                                  # 해당 연산자가 나오면
                    tmp[idx] = globals()[operator](tmp[idx-1], tmp[idx+1])                # 해당 함수 호출하여 반환된 값을 저장하고
                    tmp.pop(idx-1)                                                        # 앞, 뒤 숫자 없애주기
                    tmp.pop(idx)
                else:                                                                     # 해당 연산자가 아니면 idx += 1
                    idx += 1

        while len(tmp) != 1:                                                              # 같은 연산자가 여러개 있는 경우 상단의 for문으로 모두 제거되지 않는 문제가 있으므로
            tmp[0] = globals()[tmp[1]](tmp[0], tmp[2])                                    # tmp의 길이가 1이 될 때까지 연산해주기
            tmp.pop(1)
            tmp.pop(1)
        
        ans.append(abs(tmp[0]))
    return max(ans)


# 테스트 1 〉	통과 (0.04ms, 10.1MB)
# 테스트 2 〉	통과 (0.04ms, 10.5MB)
# 테스트 3 〉	통과 (0.06ms, 10.4MB)
# 테스트 4 〉	통과 (0.06ms, 10.5MB)
# 테스트 5 〉	통과 (0.11ms, 10.5MB)
# 테스트 6 〉	통과 (0.10ms, 10.5MB)
# 테스트 7 〉	통과 (0.08ms, 10.4MB)
# 테스트 8 〉	통과 (0.08ms, 10.4MB)
# 테스트 9 〉	통과 (0.09ms, 10.4MB)
# 테스트 10 〉	통과 (0.09ms, 10.2MB)
# 테스트 11 〉	통과 (0.09ms, 10.4MB)
# 테스트 12 〉	통과 (0.11ms, 10.4MB)
# 테스트 13 〉	통과 (0.11ms, 10.2MB)
# 테스트 14 〉	통과 (0.13ms, 10.3MB)
# 테스트 15 〉	통과 (0.13ms, 10.4MB)
# 테스트 16 〉	통과 (0.05ms, 10.4MB)
# 테스트 17 〉	통과 (0.05ms, 10.4MB)
# 테스트 18 〉	통과 (0.05ms, 10.4MB)
# 테스트 19 〉	통과 (0.04ms, 10.3MB)
# 테스트 20 〉	통과 (0.05ms, 10.3MB)
# 테스트 21 〉	통과 (0.13ms, 10.5MB)
# 테스트 22 〉	통과 (0.13ms, 10.4MB)
# 테스트 23 〉	통과 (0.04ms, 10.1MB)
# 테스트 24 〉	통과 (0.13ms, 10.4MB)
# 테스트 25 〉	통과 (0.13ms, 10.4MB)
# 테스트 26 〉	통과 (0.04ms, 10.4MB)
# 테스트 27 〉	통과 (0.13ms, 10.3MB)
# 테스트 28 〉	통과 (0.14ms, 10.3MB)
# 테스트 29 〉	통과 (0.12ms, 10.1MB)
# 테스트 30 〉	통과 (0.13ms, 10.2MB)