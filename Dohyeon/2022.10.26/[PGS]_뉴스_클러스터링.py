def solution(str1, str2):
    a = []
    b = []
    for i in range(len(str1) - 1):
        letter_A = str1[i].upper()
        letter_B = str1[i + 1].upper()
        if letter_A.isalpha() and letter_B.isalpha():
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
            if a[w1] == b[w2]:
                union -= 1
                inter += 1
                b.pop(w2)
                break
    answer = int((inter / union) * 65536)
    return answer