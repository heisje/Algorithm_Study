from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    sum_1, sum_2 = sum(queue1), sum(queue2)         # while 문 안에서 바로 sum 하니까 시간초과가 오지게 나더라구요..?
    cnt = 0

    while queue1 and queue2:                        # 둘 다 비워지면 안된다는거

        if cnt >= (len(queue1) + len(queue2)) * 2:  # 두 번씩 왕복했으면 안된다는거
            return -1

        if sum_1 == sum_2:                          # 합이 같아지면
            return cnt                              # 값을 리턴

        if sum_1 > sum_2:                           # 큰 쪽거 빼내서 넣고 sum에 더하고 빼고
            tmp = queue1.popleft()
            queue2.append(tmp)
            sum_1 -= tmp
            sum_2 += tmp
        else:
            tmp = queue2.popleft()
            queue1.append(tmp)
            sum_1 += tmp
            sum_2 -= tmp
        cnt += 1                                    # 횟수 + 1

    return -1

'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.03ms, 10.1MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (0.04ms, 10.4MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
테스트 9 〉	통과 (0.06ms, 10.2MB)
테스트 10 〉	통과 (0.15ms, 10.2MB)
테스트 11 〉	통과 (84.37ms, 14.4MB)
테스트 12 〉	통과 (19.00ms, 14.5MB)
테스트 13 〉	통과 (2.29ms, 12.1MB)
테스트 14 〉	통과 (4.15ms, 12.3MB)
테스트 15 〉	통과 (7.00ms, 18MB)
테스트 16 〉	통과 (3.40ms, 18.6MB)
테스트 17 〉	통과 (3.13ms, 17.7MB)
테스트 18 〉	통과 (10.82ms, 33.2MB)
테스트 19 〉	통과 (13.98ms, 37.5MB)
테스트 20 〉	통과 (40.08ms, 37.7MB)
테스트 21 〉	통과 (22.99ms, 37.7MB)
테스트 22 〉	통과 (91.00ms, 37.9MB)
테스트 23 〉	통과 (80.84ms, 37.8MB)
테스트 24 〉	통과 (101.24ms, 37.9MB)
테스트 25 〉	통과 (0.06ms, 10.2MB)
테스트 26 〉	통과 (0.04ms, 10MB)
테스트 27 〉	통과 (0.03ms, 10.2MB)
테스트 28 〉	통과 (141.83ms, 19.3MB)
테스트 29 〉	통과 (0.29ms, 11MB)
테스트 30 〉	통과 (78.83ms, 19.4MB)
'''