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

"""
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.05ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.2MB)
테스트 5 〉	통과 (0.25ms, 10.3MB)
테스트 6 〉	통과 (0.20ms, 10.1MB)
테스트 7 〉	통과 (0.15ms, 10.4MB)
테스트 8 〉	통과 (0.18ms, 10.3MB)
테스트 9 〉	통과 (0.31ms, 10.3MB)
테스트 10 〉	통과 (0.18ms, 10.2MB)
테스트 11 〉	통과 (0.29ms, 10MB)
테스트 12 〉	통과 (0.20ms, 10.2MB)
테스트 13 〉	통과 (0.35ms, 10.1MB)
테스트 14 〉	통과 (31.77ms, 10.4MB)
테스트 15 〉	통과 (34.78ms, 10.3MB)
테스트 16 〉	통과 (32.13ms, 10.3MB)
테스트 17 〉	통과 (1.06ms, 10.3MB)
테스트 18 〉	통과 (1.81ms, 10.2MB)
테스트 19 〉	통과 (0.47ms, 10.1MB)
테스트 20 〉	통과 (1.61ms, 10.2MB)
테스트 21 〉	통과 (15.76ms, 10.3MB)
테스트 22 〉	통과 (6.54ms, 10.4MB)
테스트 23 〉	통과 (21.09ms, 10.2MB)
테스트 24 〉	통과 (15.25ms, 10.1MB)
테스트 25 〉	통과 (20.97ms, 10.2MB)
테스트 26 〉	통과 (4.78ms, 10.3MB)
"""