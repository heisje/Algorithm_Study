def solution(str1, str2):
    answer = 0
    tmp1 = []
    for i in range(len(str1)-1):
        s = str1[i] + str1[i+1]
        if s.isalpha():
            tmp1.append(s.lower())
    tmp2 = []
    for i in range(len(str2)-1):
        s = str2[i] + str2[i+1]
        if s.isalpha():
            tmp2.append(s.lower())
    A = 0
    B = 0
    check = []
    for i in range(len(tmp1)):
        if (tmp1[i] in tmp2) and (tmp1[i] not in check):
            A += min(tmp1.count(tmp1[i]), tmp2.count(tmp1[i]))
            B += max(tmp1.count(tmp1[i]), tmp2.count(tmp1[i]))
            check.append(tmp1[i])
        elif (tmp1[i] not in tmp2) and (tmp1[i] not in check):
            B += tmp1.count(tmp1[i])
            check.append(tmp1[i])
    for j in range(len(tmp2)):
        if tmp2[j] not in check:
            B += tmp2.count(tmp2[j])
            check.append(tmp2[j])
    # print(A, B)
    if A or B:
        answer = int(65536 * (A / B))
    else:
        answer = 65536
    return answer

'''
테스트 1 〉	통과 (0.02ms, 10.4MB)
테스트 2 〉	통과 (0.04ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (16.51ms, 10.2MB)
테스트 5 〉	통과 (0.04ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.3MB)
테스트 7 〉	통과 (0.24ms, 10.3MB)
테스트 8 〉	통과 (0.02ms, 10.3MB)
테스트 9 〉	통과 (0.18ms, 10.3MB)
테스트 10 〉	통과 (0.96ms, 10.3MB)
테스트 11 〉	통과 (1.39ms, 10.4MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.09ms, 10.4MB)
'''