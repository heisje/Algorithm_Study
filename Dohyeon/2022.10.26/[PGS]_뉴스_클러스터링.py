def solution(str1, str2):
    a = []                          # 두글자씩을 넣을 리스트 두개
    b = []
    for i in range(len(str1) - 1):
        letter_A = str1[i].upper()                  # 글자와 그 다음 글자를 대문자로
        letter_B = str1[i + 1].upper()
        if letter_A.isalpha() and letter_B.isalpha():   # 둘다 알파벳이면 리스트에 넣기
            a.append(letter_A+letter_B)

    for i in range(len(str2) - 1):
        letter_A = str2[i].upper()
        letter_B = str2[i + 1].upper()
        if letter_A.isalpha() and letter_B.isalpha():
            b.append(letter_A+letter_B)

    inter = 0
    union = len(a) + len(b)
    if union == 0:
        return 65536
    for w1 in range(len(a)):
        for w2 in range(len(b)):
            if a[w1] == b[w2]:      # 같은게 있을 경우
                union -= 1          # 합집합 수 하나 뺌
                inter += 1          # 교집합 수 하나 더함
                b.pop(w2)           # 리스트에서 제거
                break
    answer = int((inter / union) * 65536)
    return answer

#테스트 1 〉	통과 (0.02ms, 10.2MB)
#테스트 2 〉	통과 (0.03ms, 10.2MB)
#테스트 3 〉	통과 (0.02ms, 10.2MB)
#테스트 4 〉	통과 (1.01ms, 10.1MB)
#테스트 5 〉	통과 (0.03ms, 10.4MB)
#테스트 6 〉	통과 (0.01ms, 10.1MB)
#테스트 7 〉	통과 (0.14ms, 10.2MB)
#테스트 8 〉	통과 (0.01ms, 10.2MB)
#테스트 9 〉	통과 (0.21ms, 10.3MB)
#테스트 10 〉	통과 (0.50ms, 10.4MB)
#테스트 11 〉	통과 (0.95ms, 10.2MB)
#테스트 12 〉	통과 (0.01ms, 10.4MB)
#테스트 13 〉	통과 (0.08ms, 10.2MB)