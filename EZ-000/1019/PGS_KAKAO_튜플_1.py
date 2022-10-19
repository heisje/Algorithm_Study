def solution(s):
    answer = []
    sets = []
    flag = 0
    num = ''
    for c in s[1:-1]:
        if c == '{':
            temp = []
            flag = 1
        elif c == '}':
            temp.append(int(num))
            num = ''
            sets.append(temp)
            flag = 0
        elif c == ',':
            if flag:
                temp.append(int(num))
                num = ''
        else:
            num += c

    sets.sort(key=lambda x: len(x))

    for elem in sets:
        for n in elem:
            if n not in answer:
                answer.append(n)

    return answer

# 테스트 1 〉	통과 (0.03ms, 10.2MB)
# 테스트 2 〉	통과 (0.03ms, 10.2MB)
# 테스트 3 〉	통과 (0.02ms, 10.4MB)
# 테스트 4 〉	통과 (0.13ms, 10.1MB)
# 테스트 5 〉	통과 (0.40ms, 10.3MB)
# 테스트 6 〉	통과 (1.15ms, 10.1MB)
# 테스트 7 〉	통과 (28.13ms, 10.9MB)
# 테스트 8 〉	통과 (140.93ms, 12.5MB)
# 테스트 9 〉	통과 (48.73ms, 11.5MB)
# 테스트 10 〉 통과 (142.84ms, 12.8MB)
# 테스트 11 〉 통과 (218.69ms, 14MB)
# 테스트 12 〉 통과 (351.65ms, 16.4MB)
# 테스트 13 〉 통과 (352.63ms, 16.3MB)
# 테스트 14 〉 통과 (415.82ms, 16.4MB)
# 테스트 15 〉 통과 (0.02ms, 10.2MB)
