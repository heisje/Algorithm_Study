def solution(s):
    answer = []
    ans_tmp = []
    num = ''
    for i in range(1, len(s)-1):
        if s[i] == '{':
            tmp = []
            
        elif s[i] == '}':
            tmp.append(int(num))
            num = ''
            ans_tmp.append(tmp[:])
            tmp = []
            
        elif s[i] == ',':
            if num:
                tmp.append(int(num))
                num = ''
            else:
                pass
            
        else:
            num += s[i]
    ans_tmp.sort(key=lambda x:len(x))
    for i in ans_tmp:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer


'''
테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.5MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.10ms, 10.3MB)
테스트 5 〉	통과 (1.11ms, 10.3MB)
테스트 6 〉	통과 (1.63ms, 10.3MB)
테스트 7 〉	통과 (40.42ms, 11MB)
테스트 8 〉	통과 (229.65ms, 12.4MB)
테스트 9 〉	통과 (78.57ms, 11.4MB)
테스트 10 〉통과 (259.32ms, 12.7MB)
테스트 11 〉통과 (343.70ms, 13.8MB)
테스트 12 〉통과 (443.46ms, 15.5MB)
테스트 13 〉통과 (543.93ms, 15.6MB)
테스트 14 〉통과 (471.36ms, 15.7MB)
테스트 15 〉통과 (0.02ms, 10.3MB)
'''