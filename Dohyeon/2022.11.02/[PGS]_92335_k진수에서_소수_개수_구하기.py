def solution(n, k):
    result = ''
    while (True):
        q = n // k
        d = n % k
        if q < k:
            result = result + str(d) + str(q)
            break
        else:
            result = result + str(d)
            n = q

    result = result[::-1]
    cnt = 0
    mini_num = ''
    for i in range(len(result)):
        if result[i] == '0':
            if mini_num:
                mini_num = int(mini_num)
                for k in range(2, int(mini_num**0.5)+1):
                    if mini_num % k == 0:
                        break
                else:
                    if mini_num != 1:
                        cnt += 1
                mini_num = ''
        else:
            mini_num += result[i]
    if mini_num:
        mini_num = int(mini_num)
        for k in range(2, int(mini_num**0.5)+1):
            if mini_num % k == 0:
                break
        else:
            if mini_num != 1:
                cnt += 1
    answer = cnt
    return answer