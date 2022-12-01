def change_to_n(num, n):
    share = num
    remains = []
    result = ''
    chart = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    while share >= n:
        temp = share % n
        remains.append(temp)
        share = share // n


    for i in range(len(remains)-1, -1, -1):

        result = result + chart[remains[i]]
    result = chart[share] + result

    return result


def solution(n, t, m, p):
    answer = ''

    num_count = 0
    t_count = 0
    number_string = ''
    while (len(number_string) < m * t):
        number_string = number_string + str(change_to_n(num_count, n))
        num_count += 1

    while (len(answer) < t):
        answer = answer + number_string[t_count * m + p - 1]
        t_count += 1

    return answer


print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))