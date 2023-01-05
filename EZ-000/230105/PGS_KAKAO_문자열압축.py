def solution(s):
    answer = 1000
    L = len(s)
    if L == 1:
        answer = 1
    else:
        for n in range(1, L // 2 + 1):
            temp = 0
            lst = [1]
            for idx in range(0, L, n):
                former, latter = s[idx:idx + n], s[idx + n:idx + 2 * n]
                if former == latter:
                    lst.append(lst[-1] + 1)
                else:
                    if lst[-1] == 1:
                        temp += n
                    else:
                        temp += len(str(lst[-1])) + n

                    if len(former) == len(latter):
                        lst.append(1)
                    else:
                        temp += len(latter)
                        break
            if temp < answer:
                answer = temp
    return answer
