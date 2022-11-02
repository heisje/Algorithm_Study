from collections import defaultdict

def solution(fees, records):
    answer = []
    DEFAULT_MIN, DEFAULT_FEE, BLOCK_MIN, BLOCK_FEE  = fees

    recode_d = defaultdict(int)  # 중간 기록용도
    recode_d_stack = defaultdict(int)  # 누적시간 기록용도
    total_fee = []  # 토탈 계산용도
    for record in records:
        # 입력받기
        time, num, status = record.split()
        hour, minute = map(int, time.split(':'))
        minute = hour * 60 + minute
        num = int(num)
        
        # IN & OUT
        if status == 'IN':
            recode_d[num] = minute
        if status == 'OUT':
            start = recode_d[num]
            end = minute
            use_time = end - start
            
            recode_d_stack[num] += use_time  # 누적 값에 추가
            recode_d[num] = -1  # 계산 완료 표시
    
    # IN만 한 애들 추가하기
    for key, value in recode_d.items():
        if value != -1:
            start = value
            end = 23 * 60 + 59 
            use_time = end - start
            recode_d_stack[key] += use_time

    # 금액 계산
    for key, value in recode_d_stack.items():
        use_time = value - DEFAULT_MIN
        result_fee = DEFAULT_FEE
        if use_time > 0:
            result_fee = DEFAULT_FEE + (use_time // BLOCK_MIN) * BLOCK_FEE
            if use_time % BLOCK_MIN:
                result_fee += BLOCK_FEE
        total_fee.append((key, result_fee))

    total_fee.sort()
    answer = [fee for _, fee in total_fee]
    print(answer)
    return answer


solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
solution([120, 0, 60, 591],["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])
solution([1, 461, 1, 10],["00:00 1234 IN"])

# 테스트 1 〉	통과 (0.05ms, 10.5MB)
# 테스트 2 〉	통과 (0.04ms, 10.5MB)
# 테스트 3 〉	통과 (0.06ms, 10.4MB)
# 테스트 4 〉	통과 (0.09ms, 10.4MB)
# 테스트 5 〉	통과 (0.22ms, 10.5MB)
# 테스트 6 〉	통과 (0.25ms, 10.5MB)
# 테스트 7 〉	통과 (1.88ms, 10.6MB)
# 테스트 8 〉	통과 (1.08ms, 10.4MB)
# 테스트 9 〉	통과 (0.23ms, 10.4MB)
# 테스트 10 〉	통과 (1.78ms, 10.6MB)
# 테스트 11 〉	통과 (2.24ms, 10.7MB)
# 테스트 12 〉	통과 (2.24ms, 10.7MB)
# 테스트 13 〉	통과 (0.04ms, 10.4MB)
# 테스트 14 〉	통과 (0.04ms, 10.5MB)
# 테스트 15 〉	통과 (0.03ms, 10.4MB)
# 테스트 16 〉	통과 (0.03ms, 10.4MB)

# LV.2 / 40분