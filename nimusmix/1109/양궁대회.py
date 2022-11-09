from collections import defaultdict

def solution(n, info):
    array = [0] * 11                                          # 라이언이 맞힌 과녁 정보를 담을 리스트
    peach = 0
    for i in range(10):                                       # info를 순회하며 어피치가 얻을 수 있는 최대 점수 계산
        peach += (10 - i) if info[i] else 0
            
    array_dict = defaultdict(list)                            # 라이언이 맞힌 과녁 정보 리스트를 점수차 별로 담을 딕셔너리
    max_diff = 1                                              # 가장 큰 점수차. 비길 경우도 어피치가 이기므로 1을 할당함.
    
    def make_array(arrow, i, array, lion, peach, info):       # 라이언이 쏠 수 있는 과녁의 경우의 수를 모두 계산할 함수 (DFS)
        nonlocal max_diff, array_dict
        
        if arrow < 0:                                         # 가지치기1. 쏜 화살이 남은 화살의 수보다 많으면 return
            return
        
        max_lion = lion + (10 - i) ** 2                       # 가지치기2. 현재 시점에서 가능한 가장 큰 점수차가 max_diff보다 작으면 return
        if max_diff > (max_lion - peach):
            return
        
        if i == 11 or arrow == 0:                             # 리스트를 다 돌았거나 남은 화살이 없을 때
            if i == 11 and arrow:                             # 리스트를 다 돌았는데 화살이 남으면 0점 과녁에 쏨.
                array[10] += arrow
                
            diff = lion - peach                               # 현재 점수차 계산
            max_diff = max(max_diff, diff)                    # max_diff 갱신
            if max_diff == diff:                              # max_diff와 현재 점수차가 같을 때 점수차를 key로 현재 과녁 정보 append
                array_dict[diff].append(array[:])
            array[10] = 0                                     # 화살이 남았을 때 더해준 경우가 있으므로 0점 과녁을 0으로 만들어주고 return
            return

        target = info[i] + 1                                  # 어피치가 (10-i)점 과녁에 쏜 화살의 수보다 1개 더 많은 수
        array[i] = target                                     # 0개의 화살을 쏘는 경우와 target개의 화살을 쏘는 경우 2가지 모두 탐색
        make_array(arrow-target, i + 1, array, (lion + 10 - i), (peach - 10 + i) if info[i] else peach, info)
        array[i] = 0
        make_array(arrow, i + 1, array, lion, peach, info)
             
    make_array(n, 0, array, 0, peach, info)

    if array_dict and len(array_dict[max_diff]) > 1:          # 가장 큰 점수차인 array가 2개 이상일 때 array들을 reverse 후 sort
        array_dict[max_diff] = sorted(list(map(lambda x: x[::-1], array_dict[max_diff])))
        return array_dict[max_diff][-1][::-1]                 # 가장 마지막에 있는 array가 가장 낮은 점수를 맞힌 경우가 마지막에 옴.
    return array_dict[max_diff][-1] if array_dict else [-1]


# 테스트 1 〉	통과 (0.03ms, 10.2MB)
# 테스트 2 〉	통과 (0.05ms, 10.4MB)
# 테스트 3 〉	통과 (0.06ms, 10.3MB)
# 테스트 4 〉	통과 (0.06ms, 10.2MB)
# 테스트 5 〉	통과 (0.06ms, 10.4MB)
# 테스트 6 〉	통과 (0.05ms, 10.3MB)
# 테스트 7 〉	통과 (0.05ms, 10.2MB)
# 테스트 8 〉	통과 (0.06ms, 10.3MB)
# 테스트 9 〉	통과 (0.05ms, 10.3MB)
# 테스트 10 〉	통과 (0.06ms, 10.3MB)
# 테스트 11 〉	통과 (0.05ms, 10.4MB)
# 테스트 12 〉	통과 (0.05ms, 10.2MB)
# 테스트 13 〉	통과 (0.07ms, 10.3MB)
# 테스트 14 〉	통과 (0.05ms, 10.4MB)
# 테스트 15 〉	통과 (0.05ms, 10.2MB)
# 테스트 16 〉	통과 (0.05ms, 10.2MB)
# 테스트 17 〉	통과 (0.06ms, 10.3MB)
# 테스트 18 〉	통과 (0.03ms, 10MB)
# 테스트 19 〉	통과 (0.02ms, 10MB)
# 테스트 20 〉	통과 (0.06ms, 10.4MB)
# 테스트 21 〉	통과 (0.05ms, 10.3MB)
# 테스트 22 〉	통과 (0.07ms, 10.4MB)
# 테스트 23 〉	통과 (0.04ms, 10.3MB)
# 테스트 24 〉	통과 (0.05ms, 10.4MB)
# 테스트 25 〉	통과 (0.04ms, 10.1MB)