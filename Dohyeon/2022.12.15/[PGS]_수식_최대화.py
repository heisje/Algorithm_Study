import itertools


def solution(expression):
    exp_list = ['+', '-', '*']
    cal_list = list(itertools.permutations(exp_list, 3))
    original = []
    answer = 0
    temp = ''
    for i in range(len(expression)):
        if expression[i].isdigit():
            temp = temp + expression[i]
        else:
            original.append(int(temp))
            temp = ''
            original.append(expression[i])
    original.append(int(temp))
    for i in range(len(cal_list)):
        contents = original[:]
        for j in range(3):
            tmp = len(contents)
            k = 0
            while k < len(contents):
                if contents[k] == cal_list[i][j]:


                    if contents[k] == '+':
                        contents[k] = contents[k - 1] + contents[k + 1]
                    elif contents[k] == '*':
                        contents[k] = contents[k - 1] * contents[k + 1]
                    else:
                        contents[k] = contents[k - 1] - contents[k + 1]
                    contents.pop(k - 1)
                    contents.pop(k)
                    k -= 2

                k += 1
        if abs(contents[0]) > answer:
            answer = abs(contents[0])
    return answer


print(solution("50*6-3*2"))

"""

테스트 1 〉	통과 (0.05ms, 10.4MB)
테스트 2 〉	통과 (0.05ms, 10.4MB)
테스트 3 〉	통과 (0.08ms, 10.4MB)
테스트 4 〉	통과 (0.08ms, 10.3MB)
테스트 5 〉	통과 (0.10ms, 10.4MB)
테스트 6 〉	통과 (0.09ms, 10.4MB)
테스트 7 〉	통과 (0.10ms, 10.4MB)
테스트 8 〉	통과 (0.11ms, 10.4MB)
테스트 9 〉	통과 (0.12ms, 10.3MB)
테스트 10 〉	통과 (0.13ms, 10.4MB)
테스트 11 〉	통과 (0.13ms, 10.4MB)
테스트 12 〉	통과 (0.14ms, 10.5MB)
테스트 13 〉	통과 (0.15ms, 10.3MB)
테스트 14 〉	통과 (0.17ms, 10.5MB)
테스트 15 〉	통과 (0.19ms, 10.5MB)
테스트 16 〉	통과 (0.06ms, 10.4MB)
테스트 17 〉	통과 (0.06ms, 10.4MB)
테스트 18 〉	통과 (0.07ms, 10.4MB)
테스트 19 〉	통과 (0.09ms, 10.5MB)
테스트 20 〉	통과 (0.06ms, 10.5MB)
테스트 21 〉	통과 (0.17ms, 10.3MB)
테스트 22 〉	통과 (0.32ms, 10.5MB)
테스트 23 〉	통과 (0.06ms, 10.4MB)
테스트 24 〉	통과 (0.18ms, 10.4MB)
테스트 25 〉	통과 (0.18ms, 10.4MB)
테스트 26 〉	통과 (0.06ms, 10.5MB)
테스트 27 〉	통과 (0.17ms, 10.4MB)
테스트 28 〉	통과 (0.19ms, 10.4MB)
테스트 29 〉	통과 (0.16ms, 10.4MB)
테스트 30 〉	통과 (0.17ms, 10.5MB)
"""