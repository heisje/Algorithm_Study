def solution(s):
    answer = len(s)

    for i in range(1, len(s)):
        word_zip = ''
        cnt = 1
        prev = s[:i]
        for j in range(i, len(s), i):
            if s[j:j+i] == prev:
                cnt += 1
            else:
                word_zip += prev if cnt == 1 else str(cnt) + prev
                cnt = 1
                prev = s[j:j+i]
        word_zip += prev if cnt == 1 else str(cnt) + prev
        answer = min(answer, len(word_zip))
    return answer


print(solution("aabbaccc"))
