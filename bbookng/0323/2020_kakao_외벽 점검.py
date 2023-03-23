from collections import deque
def check(point, weak, distance, n):
    result = []
    for x in weak:
        if not (point <= x <= point + distance or (x < point and x <= point + distance - n)):
            result.append(x)

    return tuple(result)


def solution(n, weak, dist):
    dist.sort(reverse=True)
    q = deque([weak])
    visited = set()
    visited.add(tuple(weak))

    for i, d in enumerate(dist):
        for _ in range(len(q)):
            arr = q.popleft()
            for j in arr:
                repair = check(j, arr, d, n)
                if not repair:
                    return i + 1
                elif repair not in visited:
                    visited.add(repair)
                    q.append(list(repair))
    return -1

'''
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.06ms, 10.1MB)
테스트 3 〉	통과 (20.57ms, 10.3MB)
테스트 4 〉	통과 (4.79ms, 10.2MB)
테스트 5 〉	통과 (1.34ms, 10.3MB)
테스트 6 〉	통과 (9.08ms, 10.6MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.10ms, 10.2MB)
테스트 9 〉	통과 (0.09ms, 10.2MB)
테스트 10 〉	통과 (42.91ms, 11.5MB)
테스트 11 〉	통과 (22.29ms, 10.5MB)
테스트 12 〉	통과 (24.99ms, 10.6MB)
테스트 13 〉	통과 (210.43ms, 15.2MB)
테스트 14 〉	통과 (71.44ms, 11.7MB)
테스트 15 〉	통과 (18.22ms, 10.4MB)
테스트 16 〉	통과 (0.53ms, 10.3MB)
테스트 17 〉	통과 (3.14ms, 10.2MB)
테스트 18 〉	통과 (1.23ms, 10.2MB)
테스트 19 〉	통과 (0.07ms, 10.1MB)
테스트 20 〉	통과 (0.41ms, 10.3MB)
테스트 21 〉	통과 (0.06ms, 10.2MB)
테스트 22 〉	통과 (0.63ms, 10.2MB)
테스트 23 〉	통과 (1.51ms, 10.2MB)
테스트 24 〉	통과 (2.15ms, 10.2MB)
테스트 25 〉	통과 (0.16ms, 10.2MB)
'''