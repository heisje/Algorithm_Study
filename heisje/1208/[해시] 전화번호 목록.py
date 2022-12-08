# https://school.programmers.co.kr/learn/courses/30/lessons/42577
from collections import defaultdict

def solution(phone_book):
    answer = True
    all_dict = defaultdict(list)
    # 무조건 접두사가 늦게 나올 수 있게 배치해놓고 sort
    phone_book.sort(reverse=True)
    for idx, phone in enumerate(phone_book):

        # 모든 문자열을 쪼개서 전부 dict에 넣어둔다.
        for ph in range(1,len(phone)+1):
            all_dict[phone[:ph]].append(idx+1)

        # 2개이상이면, 접두사가 충족하는 문자열이 있다는 것이므로 break
        if len(all_dict[phone]) > 1:
            answer = False
            break
    return answer

solution(["119", "97674223", "1195524421"])
solution(["123","456","789"])
solution(["12","123","1235","567","88"])


# 테스트 1 〉	통과 (0.02ms, 10.1MB)
# 테스트 2 〉	통과 (0.02ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.02ms, 10.3MB)
# 테스트 5 〉	통과 (0.02ms, 10.3MB)
# 테스트 6 〉	통과 (0.02ms, 10.2MB)
# 테스트 7 〉	통과 (0.01ms, 10.2MB)
# 테스트 8 〉	통과 (0.02ms, 10.1MB)
# 테스트 9 〉	통과 (0.01ms, 10.2MB)
# 테스트 10 〉	통과 (0.01ms, 10MB)
# 테스트 11 〉	통과 (0.02ms, 10.1MB)
# 테스트 12 〉	통과 (0.01ms, 10.1MB)
# 테스트 13 〉	통과 (0.01ms, 10.1MB)
# 테스트 14 〉	통과 (4.82ms, 11.8MB)
# 테스트 15 〉	통과 (1.65ms, 10.5MB)
# 테스트 16 〉	통과 (15.96ms, 16.5MB)
# 테스트 17 〉	통과 (20.82ms, 17.7MB)
# 테스트 18 〉	통과 (23.05ms, 18.3MB)
# 테스트 19 〉	통과 (22.13ms, 18.5MB)
# 테스트 20 〉	통과 (18.86ms, 16.5MB)
# ----------------------------------
# 테스트 1 〉	통과 (3.22ms, 10.6MB)
# 테스트 2 〉	통과 (2.91ms, 10.7MB)
# 테스트 3 〉	통과 (1258.20ms, 226MB)
# 테스트 4 〉	통과 (1046.93ms, 226MB)