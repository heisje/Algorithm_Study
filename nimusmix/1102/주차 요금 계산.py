from collections import defaultdict

def solution(fees, records):
    BASE_M, BASE_F, PER_M, PER_F = fees
    
    in_dict = defaultdict(list)
    out_dict = defaultdict(list)
    fees_dict = defaultdict(int)
    
    for i in records:
        time, car, status = i.split()
        h, m = map(int, time.split(':'))
        car = int(car)

        if status == "IN":
            in_dict[car].append((h, m))
        else:
            out_dict[car].append((h, m))
    
    for c in in_dict.keys():
        while in_dict[c]:
            in_h, in_m = in_dict[c].pop(0)

            if out_dict[c]:
                out_h, out_m = out_dict[c].pop(0)
            else:
                out_h, out_m = 23, 59
            
            start = in_h * 60 + in_m
            end = out_h * 60 + out_m
             
            fees_dict[c] += end - start

    for i in fees_dict.keys():
        rst = fees_dict[i]
        fees_dict[i] = BASE_F

        if rst > BASE_M:
            rst -= BASE_M
            if rst % PER_M:
                fees_dict[i] += (rst // PER_M + 1) * PER_F
            else:
                fees_dict[i] += (rst // PER_M) * PER_F
    
    answer = [i[1] for i in sorted(fees_dict.items())]
    return answer


# 테스트 1 〉	통과 (0.05ms, 10.4MB)
# 테스트 2 〉	통과 (0.04ms, 10.4MB)
# 테스트 3 〉	통과 (0.05ms, 10.4MB)
# 테스트 4 〉	통과 (0.09ms, 10.4MB)
# 테스트 5 〉	통과 (0.22ms, 10.4MB)
# 테스트 6 〉	통과 (0.23ms, 10.5MB)
# 테스트 7 〉	통과 (2.03ms, 10.6MB)
# 테스트 8 〉	통과 (1.09ms, 10.5MB)
# 테스트 9 〉	통과 (0.24ms, 10.5MB)
# 테스트 10 〉	통과 (1.68ms, 10.5MB)
# 테스트 11 〉	통과 (2.20ms, 10.7MB)
# 테스트 12 〉	통과 (2.29ms, 10.7MB)
# 테스트 13 〉	통과 (0.06ms, 10.4MB)
# 테스트 14 〉	통과 (0.03ms, 10.3MB)
# 테스트 15 〉	통과 (0.03ms, 10.4MB)
# 테스트 16 〉	통과 (0.03ms, 10.5MB)