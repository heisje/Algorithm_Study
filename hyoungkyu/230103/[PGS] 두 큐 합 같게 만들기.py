# Lv2
from collections import deque

def solution(queue1, queue2):
    answer = -1
    que1 = deque(queue1)
    que2 = deque(queue2)
    tot1 = sum(queue1)
    tot2 = sum(queue2)
    cnt = 0
    L = 3*len(queue1)           # que1과 que2의 길이가 같고 양쪽 전부 다 옮길 때까지 반복
                                # que1을 마지막 빼고 전부 que2로 옮긴 다음 다시 que2를 마지막 빼고 전부 que1으로 옮길 경우
                                # que1 -> que2 : l
                                # que2 -> que1 : 2*l
    
    while cnt < L:
        if tot1 == tot2:
            answer = cnt
            break
        cnt += 1
        if tot1 > tot2:
            tmp = que1.popleft()
            que2.append(tmp)
            tot1 -= tmp
            tot2 += tmp
        else:
            tmp = que2.popleft()
            que1.append(tmp)
            tot1 += tmp
            tot2 -= tmp
    
    return answer

'''
테스트 1 〉통과 (0.94ms, 10.3MB)
테스트 2 〉통과 (0.71ms, 10.1MB)
테스트 3 〉통과 (0.01ms, 10.2MB)
테스트 4 〉통과 (0.01ms, 10.2MB)
테스트 5 〉통과 (0.02ms, 10.1MB)
테스트 6 〉통과 (0.03ms, 10.2MB)
테스트 7 〉통과 (0.02ms, 10.1MB)
테스트 8 〉통과 (0.02ms, 10.2MB)
테스트 9 〉통과 (0.09ms, 10.3MB)
테스트 10 〉통과 (0.10ms, 10.1MB)
테스트 11 〉통과 (29.52ms, 14.6MB)
테스트 12 〉통과 (5.78ms, 14.7MB)
테스트 13 〉통과 (3.53ms, 12.2MB)
테스트 14 〉통과 (2.40ms, 12.3MB)
테스트 15 〉통과 (6.33ms, 18MB)
테스트 16 〉통과 (3.17ms, 18.4MB)
테스트 17 〉통과 (3.16ms, 17.7MB)
테스트 18 〉통과 (11.06ms, 33.1MB)
테스트 19 〉통과 (11.71ms, 37.3MB)
테스트 20 〉통과 (28.07ms, 37.8MB)
테스트 21 〉통과 (18.59ms, 37.8MB)
테스트 22 〉통과 (52.26ms, 37.7MB)
테스트 23 〉통과 (42.38ms, 37.8MB)
테스트 24 〉통과 (62.07ms, 37.8MB)
테스트 25 〉통과 (0.04ms, 10.2MB)
테스트 26 〉통과 (0.02ms, 10.2MB)
테스트 27 〉통과 (0.02ms, 10.1MB)
테스트 28 〉통과 (61.65ms, 19.4MB)
테스트 29 〉통과 (0.44ms, 10.7MB)
테스트 30 〉통과 (47.45ms, 19.2MB)
'''