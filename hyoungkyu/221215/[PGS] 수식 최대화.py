import itertools

def solution(expression):
    answer = 0
    # 숫자 리스트, 연산 리스트 나누기
    nums = []
    ops = []
    tmp = ""
    for i in expression:
        if not 48 <= ord(i) <=57:
            ops.append(i)
            nums.append(int(tmp))
            tmp = ""
        else:
            tmp += i
    if tmp:
        nums.append(int(tmp))
    
    # 연산 기호별 계산 함수
    def oper(op, num1, num2):
        if op == "*":
            return num1*num2
        elif op == "+":
            return num1+num2
        elif op == "-":
            return num1-num2
    
    # 경우의 수
    for permutation in itertools.permutations(["*", "+", "-"]):
        nums_tmp = nums[:]
        ops_tmp = ops[:]
        # 우선순위별 계산 후 리스트에 추가하는 방식
        for i in range(3):
            j = -1
            while j < len(ops_tmp)-1:
                j += 1
                # 계산을 한 후 숫자리스트에 추가하고 해당 인덱스에서 다시 시작
                if ops_tmp[j] == permutation[i]:
                    num1 = nums_tmp.pop(j)
                    num2 = nums_tmp.pop(j)
                    op = ops_tmp.pop(j)
                    nums_tmp.insert(j, oper(op, num1, num2))
                    j -= 1
        if answer < abs(nums_tmp[0]):
            answer = abs(nums_tmp[0])
            
    return answer

'''
테스트 1 〉통과 (0.07ms, 10.5MB)
테스트 2 〉통과 (0.05ms, 10.5MB)
테스트 3 〉통과 (0.06ms, 10.3MB)
테스트 4 〉통과 (0.07ms, 10.3MB)
테스트 5 〉통과 (0.08ms, 10.4MB)
테스트 6 〉통과 (0.08ms, 10.3MB)
테스트 7 〉통과 (0.08ms, 10.4MB)
테스트 8 〉통과 (0.09ms, 10.4MB)
테스트 9 〉통과 (0.17ms, 10.5MB)
테스트 10 〉통과 (0.11ms, 10.3MB)
테스트 11 〉통과 (0.16ms, 10.3MB)
테스트 12 〉통과 (0.12ms, 10.3MB)
테스트 13 〉통과 (0.12ms, 10.3MB)
테스트 14 〉통과 (0.23ms, 10.4MB)
테스트 15 〉통과 (0.26ms, 10.5MB)
테스트 16 〉통과 (0.07ms, 10.3MB)
테스트 17 〉통과 (0.08ms, 10.4MB)
테스트 18 〉통과 (0.08ms, 10.4MB)
테스트 19 〉통과 (0.05ms, 10.4MB)
테스트 20 〉통과 (0.09ms, 10.4MB)
테스트 21 〉통과 (0.15ms, 10.4MB)
테스트 22 〉통과 (0.25ms, 10.5MB)
테스트 23 〉통과 (0.07ms, 10.3MB)
테스트 24 〉통과 (0.15ms, 10.4MB)
테스트 25 〉통과 (0.15ms, 10.4MB)
테스트 26 〉통과 (0.07ms, 10.3MB)
테스트 27 〉통과 (0.25ms, 10.3MB)
테스트 28 〉통과 (0.15ms, 10.5MB)
테스트 29 〉통과 (0.14ms, 10.5MB)
테스트 30 〉통과 (0.14ms, 10.3MB)
'''