from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)

    count = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total_sum = sum1 + sum2
    max_len = len(queue1) * 3
    if total_sum % 2:
        return -1
    elif sum1 == sum2:
        return 0
    else:
        while sum1 != sum2:
            if sum1 > sum2:
                temp = queue1.popleft()
                queue2.append(temp)
                sum1 -= temp
                sum2 += temp
                count += 1
            else:
                temp = queue2.popleft()
                queue1.append(temp)
                sum2 -= temp
                sum1 += temp
                count += 1

            if count > max_len:
                return -1

        return count

print(solution([1,1,1,8,10,9], [1,1,1,1,1,1]))  # 예외 조심


"""
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.4MB)
테스트 8 〉	통과 (0.03ms, 10.4MB)
테스트 9 〉	통과 (0.05ms, 10.3MB)
테스트 10 〉	통과 (0.11ms, 10.3MB)
테스트 11 〉	통과 (31.32ms, 14.7MB)
테스트 12 〉	통과 (6.18ms, 14.7MB)
테스트 13 〉	통과 (2.14ms, 12.3MB)
테스트 14 〉	통과 (2.44ms, 12.4MB)
테스트 15 〉	통과 (5.46ms, 18MB)
테스트 16 〉	통과 (3.64ms, 18.6MB)
테스트 17 〉	통과 (3.25ms, 17.7MB)
테스트 18 〉	통과 (10.71ms, 33.2MB)
테스트 19 〉	통과 (12.95ms, 37.4MB)
테스트 20 〉	통과 (26.83ms, 37.8MB)
테스트 21 〉	통과 (20.47ms, 37.9MB)
테스트 22 〉	통과 (61.11ms, 37.9MB)
테스트 23 〉	통과 (42.94ms, 38.2MB)
테스트 24 〉	통과 (62.42ms, 38MB)
테스트 25 〉	통과 (0.04ms, 10.2MB)
테스트 26 〉	통과 (0.03ms, 10.3MB)
테스트 27 〉	통과 (0.02ms, 10.3MB)
테스트 28 〉	통과 (58.60ms, 19.3MB)
테스트 29 〉	통과 (0.48ms, 11.1MB)
테스트 30 〉	통과 (43.90ms, 19.4MB)
"""


"""
def solution(queue1, queue2):
    count = 0
    total_sum = sum(queue1) + sum(queue2)
    total_len = len(queue1) + len(queue2)
    if total_sum % 2:
        return -1
    target = total_sum // 2
    total_list = queue1 + queue2
    check = False
    for i in range(total_len):
        if sum(total_list[:i]) > target:
            break
        for j in range(i, total_len):
            if sum(total_list[i:j]) > target:
                break
            if sum(total_list[:i]) + sum(total_list[j:]) == target:
                check = True
                count = i + j - len(queue1)
                break
        if check:
            break
    if not check:
        return -1
    return count
"""