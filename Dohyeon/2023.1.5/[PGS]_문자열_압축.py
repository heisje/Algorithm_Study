def solution(s):
    min_len = len(s)
    total = ""
    for i in range(1, len(s)):
        word = s[:i]
        len_word = len(word)
        count = 1
        skip = 0
        for j in range(i, len(s)):
            if skip:
                skip -= 1
                continue
            if s[j:j+len_word] == word:
                count += 1
                skip = len_word - 1
                continue
            else:
                if count > 1:
                    total = total + str(count) + word
                else:
                    total = total + word
                word = s[j:j+i]
                count = 1
                skip = len_word - 1

        else:
            if count > 1:
                total = total + str(count) + word
            else:
                total = total + word

            if len(total) < min_len:
                min_len = len(total)
            total = ""
    return min_len

"""
테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (1.03ms, 10.2MB)
테스트 3 〉	통과 (0.39ms, 10.2MB)
테스트 4 〉	통과 (0.04ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.10ms, 10.2MB)
테스트 7 〉	통과 (2.34ms, 10.2MB)
테스트 8 〉	통과 (1.20ms, 10.1MB)
테스트 9 〉	통과 (2.20ms, 10.2MB)
테스트 10 〉	통과 (22.30ms, 10.3MB)
테스트 11 〉	통과 (0.14ms, 10.1MB)
테스트 12 〉	통과 (0.27ms, 10.2MB)
테스트 13 〉	통과 (0.18ms, 10.3MB)
테스트 14 〉	통과 (2.17ms, 10.4MB)
테스트 15 〉	통과 (0.18ms, 10.2MB)
테스트 16 〉	통과 (0.02ms, 10.2MB)
테스트 17 〉	통과 (5.77ms, 10.2MB)
테스트 18 〉	통과 (6.35ms, 10.3MB)
테스트 19 〉	통과 (9.94ms, 10.3MB)
테스트 20 〉	통과 (23.59ms, 10.2MB)
테스트 21 〉	통과 (24.10ms, 10.3MB)
테스트 22 〉	통과 (23.47ms, 10.4MB)
테스트 23 〉	통과 (24.78ms, 10.4MB)
테스트 24 〉	통과 (21.74ms, 10.3MB)
테스트 25 〉	통과 (34.15ms, 10.4MB)
테스트 26 〉	통과 (24.97ms, 10.4MB)
테스트 27 〉	통과 (32.50ms, 10.2MB)
테스트 28 〉	통과 (0.03ms, 10.3MB)
"""