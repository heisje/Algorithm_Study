from collections import Counter


def solution(clothes):
    answer = 1
    clothes = dict(clothes)
    v = clothes.values()
    c = Counter(v)

    for i in c:
        answer *= c[i] + 1
    answer = answer - 1

    return answer


"""
테스트 1 〉	통과 (0.04ms, 9.96MB)
테스트 2 〉	통과 (0.05ms, 10.2MB)
테스트 3 〉	통과 (0.04ms, 10.3MB)
테스트 4 〉	통과 (0.04ms, 10.2MB)
테스트 5 〉	통과 (0.05ms, 9.99MB)
테스트 6 〉	통과 (0.04ms, 10.1MB)
테스트 7 〉	통과 (0.05ms, 10.2MB)
테스트 8 〉	통과 (0.06ms, 9.95MB)
테스트 9 〉	통과 (0.05ms, 10MB)
테스트 10 〉	통과 (0.05ms, 10.2MB)
테스트 11 〉	통과 (0.04ms, 10.1MB)
테스트 12 〉	통과 (0.05ms, 10MB)
테스트 13 〉	통과 (0.03ms, 10.1MB)
테스트 14 〉	통과 (0.03ms, 9.95MB)
테스트 15 〉	통과 (0.03ms, 10.1MB)
테스트 16 〉	통과 (0.04ms, 10.1MB)
테스트 17 〉	통과 (0.04ms, 10.2MB)
테스트 18 〉	통과 (0.03ms, 9.94MB)
테스트 19 〉	통과 (0.04ms, 10.2MB)
테스트 20 〉	통과 (0.05ms, 9.96MB)
테스트 21 〉	통과 (0.04ms, 10.1MB)
테스트 22 〉	통과 (0.05ms, 10.2MB)
테스트 23 〉	통과 (0.03ms, 10.2MB)
테스트 24 〉	통과 (0.04ms, 10MB)
테스트 25 〉	통과 (0.05ms, 10.2MB)
테스트 26 〉	통과 (0.03ms, 9.96MB)
테스트 27 〉	통과 (0.02ms, 10.4MB)
테스트 28 〉	통과 (0.05ms, 10.2MB)
"""
