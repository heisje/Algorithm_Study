# https://school.programmers.co.kr/learn/courses/30/lessons/67257
from itertools import permutations
import re


def solution(expression):
    used = set()
    list_ex = []

    # 이렇게 할 수도 있다.
    used = [x for x in ['*','+','-'] if x in expression]
    list_ex = re.split(r'(\D)',expression)
    
    # 연산자랑 숫자랑 나눠서 리스트를 생성하는 과정
    # temp = ""
    # for i in expression:
    #     if i.isdigit():
    #         temp += i
    #     else:
    #         list_ex.append(temp)
    #         temp = ""
    #         used.add(i)
    #         list_ex.append(i)
    # list_ex.append(temp)
    # print(list_ex)
    
    # 결과값 저장
    max_result = 0
    # 우선순위를 만들고
    for crud in permutations(used, len(used)):
        list_ex_copy = list_ex[:]
        result = 0
        # 우선순위 대로 돌면서
        for choice in crud:

            #우선순위에 맞는 연산을 전부 수행시킨다.
            for idx, value in enumerate(list_ex_copy):
                # 연산자를 찾으면
                if choice == value:
                    # 연산을 수행
                    result = 0
                    front = 1
                    back = 1
                    # 비어있으면 왔다리 갔다리 하면서 찾는다.
                    while list_ex_copy[idx-front] == "":
                        front += 1
                    while list_ex_copy[idx+back] == "":
                        back += 1
                    front_val = int(list_ex_copy[idx-front])
                    back_val = int(list_ex_copy[idx+back])
                    
                    # 주어진 연산 시행
                    if choice == "*":
                        result = front_val * back_val
                    if choice == "+":
                        result = front_val + back_val
                    if choice == "-":
                        result = front_val - back_val
                    
                    # 결과를 중간값만 제대로 된걸로 만드러버려!
                    list_ex_copy[idx-front] = ""
                    list_ex_copy[idx] = result
                    list_ex_copy[idx+back] = ""

        if max_result < abs(result):
            max_result = abs(result)
    return max_result

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))


# 테스트 1 〉	통과 (0.03ms, 10.5MB)
# 테스트 2 〉	통과 (0.03ms, 10.5MB)
# 테스트 3 〉	통과 (0.07ms, 10.5MB)
# 테스트 4 〉	통과 (0.08ms, 10.5MB)
# 테스트 5 〉	통과 (0.09ms, 10.4MB)
# 테스트 6 〉	통과 (0.14ms, 10.4MB)
# 테스트 7 〉	통과 (0.16ms, 10.4MB)
# 테스트 8 〉	통과 (0.10ms, 10.4MB)
# 테스트 9 〉	통과 (0.19ms, 10.4MB)
# 테스트 10 〉	통과 (0.13ms, 10.4MB)
# 테스트 11 〉	통과 (0.11ms, 10.5MB)
# 테스트 12 〉	통과 (0.14ms, 10.4MB)
# 테스트 13 〉	통과 (0.15ms, 10.5MB)
# 테스트 14 〉	통과 (0.17ms, 10.4MB)
# 테스트 15 〉	통과 (0.18ms, 10.4MB)
# 테스트 16 〉	통과 (0.05ms, 10.6MB)
# 테스트 17 〉	통과 (0.06ms, 10.6MB)
# 테스트 18 〉	통과 (0.04ms, 10.4MB)
# 테스트 19 〉	통과 (0.04ms, 10.4MB)
# 테스트 20 〉	통과 (0.04ms, 10.4MB)
# 테스트 21 〉	통과 (0.11ms, 10.4MB)
# 테스트 22 〉	통과 (0.06ms, 10.5MB)
# 테스트 23 〉	통과 (0.03ms, 10.5MB)
# 테스트 24 〉	통과 (0.19ms, 10.5MB)
# 테스트 25 〉	통과 (0.31ms, 10.4MB)
# 테스트 26 〉	통과 (0.04ms, 10.5MB)
# 테스트 27 〉	통과 (0.34ms, 10.4MB)
# 테스트 28 〉	통과 (0.13ms, 10.4MB)
# 테스트 29 〉	통과 (0.07ms, 10.5MB)
# 테스트 30 〉	통과 (0.14ms, 10.4MB)