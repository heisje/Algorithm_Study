def solution(cap, n, deliveries, pickups):
    answer = 0
    del_idx, pick_idx = n-1, n-1
    while True:
        del_cnt = 0
        pick_cnt = 0
        del_start = del_idx
        pick_start = pick_idx
        del_idx = -1
        pick_idx = -1
        for i in range(del_start, -1, -1):
            if deliveries[i]:
                if del_cnt + deliveries[i] < cap:
                    del_cnt += deliveries[i]
                    deliveries[i] = 0
                else:
                    deliveries[i] -= cap - del_cnt
                    del_cnt = cap
                if del_idx == -1:
                    del_idx = i
                if del_cnt == cap: break
            
        for i in range(pick_start, -1, -1):
            if pickups[i]:
                if pick_cnt + pickups[i] < cap:
                    pick_cnt += pickups[i]
                    pickups[i] = 0
                else:
                    pickups[i] -= cap - pick_cnt
                    pick_cnt = cap
                if pick_idx == -1:
                    pick_idx = i
                if pick_cnt == cap: break
                
        if del_idx == -1 and pick_idx == -1:
            break
        else:
            answer += max(del_idx+1, pick_idx+1) * 2

    return answer

'''
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.00ms, 10MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.05ms, 10.2MB)
테스트 5 〉	통과 (0.05ms, 10.3MB)
테스트 6 〉	통과 (0.04ms, 10.3MB)
테스트 7 〉	통과 (0.84ms, 10.3MB)
테스트 8 〉	통과 (2.28ms, 10.3MB)
테스트 9 〉	통과 (10.60ms, 10.2MB)
테스트 10 〉	통과 (8.22ms, 10.2MB)
테스트 11 〉	통과 (3.92ms, 10.3MB)
테스트 12 〉	통과 (2.92ms, 10.4MB)
테스트 13 〉	통과 (2.35ms, 10.2MB)
테스트 14 〉	통과 (2.40ms, 10.4MB)
테스트 15 〉	통과 (32.54ms, 11.8MB)
테스트 16 〉	통과 (2659.63ms, 11.6MB)
테스트 17 〉	통과 (216.04ms, 11.7MB)
테스트 18 〉	통과 (104.85ms, 11.7MB)
테스트 19 〉	통과 (65.44ms, 11.4MB)
테스트 20 〉	통과 (90.09ms, 11.7MB)
'''