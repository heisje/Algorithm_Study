from collections import deque

def solution(s):
    answer = []

    s2 = s[2:-2].split('},{')

    s2.sort(key=lambda x:len(x))

    for i in s2:
        i = list(map(int, i.split(',')))
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))

    return(answer)

s = "{{20,111},{111}}"
print(solution(s))

'''
테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.4MB)
테스트 4 〉	통과 (0.05ms, 10.4MB)
테스트 5 〉	통과 (0.27ms, 10.3MB)
테스트 6 〉	통과 (0.68ms, 10.3MB)
테스트 7 〉	통과 (20.40ms, 10.5MB)
테스트 8 〉	통과 (105.12ms, 10.9MB)
테스트 9 〉	통과 (59.35ms, 10.5MB)
테스트 10 〉	통과 (114.74ms, 10.8MB)
테스트 11 〉	통과 (177.04ms, 11.1MB)
테스트 12 〉	통과 (311.56ms, 12.1MB)
테스트 13 〉	통과 (304.71ms, 11.9MB)
테스트 14 〉	통과 (347.25ms, 12.1MB)
테스트 15 〉	통과 (0.02ms, 10.3MB)
'''