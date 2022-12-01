def solution(n, t, m, p):
    answer=""
    full_str = ''
    total_num = 0
    i = 0  # 몇번째 p인지
    while True:
        temp = []
        # num에 해당하는 진법 구하기
        num = total_num
        while True:
            confirm = num % n #**(indices)
            num = num // n #**(indices)
            if confirm >= 10:
                confirm = chr(ord('A') + confirm - 10)
                # print(confirm)
            temp.append(confirm)
            if num <= 0:
                break
        temp.reverse()
        full_str += ''.join(map(str,temp))
        # print(full_str)

        total_num += 1


        # 쓸 수 있는 정답이 존재하면
        if len(full_str) > p-1+m*i:
            # 정답을 처리하고
            answer += full_str[p-1+m*i]
            i += 1
            #개수를 차감한다.
            t -= 1
            if t == 0:
                break
    return answer

print(solution(2,4,2,1))
print(solution(16,16,2,1))
print(solution(16,16,2,2))