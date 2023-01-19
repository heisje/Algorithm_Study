from itertools import combinations

def solution(relation):
    candidate_key = []  # 후보키
    result = []         # 유일성과 최소성을 만족하는 후보키 결과 리스트

    for i in range(1, len(relation[0])+1):
        candidate_key.extend(combinations([j for j in range(len(relation[0]))], i))

    for candidate in candidate_key:
        tmp = [tuple([relate[i] for i in candidate]) for relate in relation]

        if len(set(tmp)) == len(relation):              # 유일성 만족
            for key in result:
                if set(key).issubset(set(candidate)):   # 최소성 불만족
                    break
            else:                                       # 최소성 만족
                result.append(candidate)

    return len(result)


'''
테스트 1 〉	통과 (0.04ms, 10.1MB)
테스트 2 〉	통과 (0.04ms, 10.4MB)
테스트 3 〉	통과 (0.04ms, 10.3MB)
테스트 4 〉	통과 (0.05ms, 10MB)
테스트 5 〉	통과 (0.05ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.08ms, 10.3MB)
테스트 10 〉	통과 (0.11ms, 10.3MB)
테스트 11 〉	통과 (0.31ms, 10.3MB)
테스트 12 〉	통과 (0.99ms, 10.2MB)
테스트 13 〉	통과 (0.39ms, 10.2MB)
테스트 14 〉	통과 (0.05ms, 10.1MB)
테스트 15 〉	통과 (0.06ms, 10.4MB)
테스트 16 〉	통과 (0.05ms, 10.2MB)
테스트 17 〉	통과 (0.05ms, 10.3MB)
테스트 18 〉	통과 (2.66ms, 10.2MB)
테스트 19 〉	통과 (1.39ms, 10.2MB)
테스트 20 〉	통과 (2.64ms, 10.2MB)
테스트 21 〉	통과 (1.93ms, 10.1MB)
테스트 22 〉	통과 (1.11ms, 10.4MB)
테스트 23 〉	통과 (0.06ms, 10.4MB)
테스트 24 〉	통과 (1.30ms, 9.97MB)
테스트 25 〉	통과 (2.32ms, 10.3MB)
테스트 26 〉	통과 (1.71ms, 10.2MB)
테스트 27 〉	통과 (0.28ms, 10.4MB)
테스트 28 〉	통과 (0.72ms, 10.2MB)
'''

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))