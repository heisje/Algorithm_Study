from itertools import permutations

def solution(n, weak, dist):
    weak_n = len(weak)
    dist_n = len(dist)
    for i in range(weak_n): # 반시계 방향을 선형으로 만들기
        weak.append(weak[i] + n)

    answer = dist_n + 1
    dist_list = list(permutations(dist, dist_n)) # 순열을 이용하여 친구들의 거리를 정렬하는 모든 경우의 수 저장!

    for j in range(weak_n):
        # test_weak : 시작할 j를 정해 체크 가능한 성벽 리스트를 저장한다.
        test_weak = [weak[k] for k in range(j, j + weak_n)]
        for d in range(len(dist_list)): # 친구들의 정렬에 따른 모든 경우 체크!
            # 초기 설정
            friend_idx = 0
            cnt = 1
            friend_max_d = test_weak[0] + dist_list[d][0] # 첫번째 친구가 이동할 수 있는 최대 거리
            flag = True
            # 외벽 점검 가능한지 확인하는 부분
            for w in range(weak_n):
                if test_weak[w] > friend_max_d: # 확인할 수 있는 거리를 넘은 경우
                    friend_idx += 1 # 다음 친구 투입!
                    cnt += 1
                    if cnt > dist_n: # 투입할 친구가 없는 경우
                        flag = False
                        break
                    friend_max_d = test_weak[w] + dist_list[d][friend_idx] # 최대 확인할 수 있는 거리 갱신
            if flag and answer > cnt:
                answer = cnt
    if answer == dist_n + 1: answer = -1 # 외벽 점검이 불가능한 경우 -1로 출력할 조건
    return answer