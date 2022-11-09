from itertools import combinations_with_replacement

def solution(n, info):
    answer = []
    max_ = 0

    # 중복조합 이용해서 모든 경우의 수를 순회
    for i in list(combinations_with_replacement(range(0, 11), n)):
        # ryan의 점수 list
        tmp = [0] * 11

        print(i)

        # 조합 대로 점수에 카운팅
        for j in i:
            tmp[10 - j] += 1

        ryan = 0
        apeach = 0

        # 10점까지 돌면서
        for k in range(11):
            R, A = tmp[k], info[k]

            if R == A == 0:             # 둘 다 0 이면 무의미
                continue
            if R > A:                   # 라이언이 더 크면
                ryan += (10 - k)        # ㄹㅏ이언에 점수 더하기
            else:                       # 어피치가 더 크면
                apeach += (10 - k)      # 어피치 점수 더하기

        if ryan > apeach:               # 총 점수 크면
            if max_ < (ryan - apeach):  # max 값 갱신
                max_ = ryan - apeach
                answer = tmp            # 정답도 갱신

    if not answer:                      # 못이기면
        return [-1]                     # -1 return
    return answer

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))


'''
테스트 1 〉	통과 (0.19ms, 10.2MB)
테스트 2 〉	통과 (248.10ms, 20.7MB)
테스트 3 〉	통과 (324.81ms, 20.8MB)
테스트 4 〉	통과 (5.68ms, 10.3MB)
테스트 5 〉	통과 (512.98ms, 34.7MB)
테스트 6 〉	통과 (468.60ms, 34.8MB)
테스트 7 〉	통과 (5.69ms, 10.3MB)
테스트 8 〉	통과 (0.49ms, 10.1MB)
테스트 9 〉	통과 (6.10ms, 10.3MB)
테스트 10 〉	통과 (0.81ms, 10.3MB)
테스트 11 〉	통과 (3.64ms, 10.2MB)
테스트 12 〉	통과 (2.09ms, 10.4MB)
테스트 13 〉	통과 (43.52ms, 12MB)
테스트 14 〉	통과 (238.70ms, 20.8MB)
테스트 15 〉	통과 (217.55ms, 20.7MB)
테스트 16 〉	통과 (30.40ms, 10.7MB)
테스트 17 〉	통과 (5.80ms, 10.3MB)
테스트 18 〉	통과 (0.15ms, 10.1MB)
테스트 19 〉	통과 (0.03ms, 10.3MB)
테스트 20 〉	통과 (231.55ms, 20.7MB)
테스트 21 〉	통과 (225.27ms, 20.8MB)
테스트 22 〉	통과 (493.35ms, 34.7MB)
테스트 23 〉	통과 (0.48ms, 10.4MB)
테스트 24 〉	통과 (471.90ms, 34.7MB)
테스트 25 〉	통과 (581.11ms, 34.7MB)
'''