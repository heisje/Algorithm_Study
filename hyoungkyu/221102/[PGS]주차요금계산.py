
def solution(fees, records):
    def hour(IN, OUT):
        in_H, in_M = map(int, IN.split(':'))
        out_H, out_M = map(int, OUT.split(':'))
        if in_M <= out_M:
            minute = 60*(out_H-in_H) + (out_M-in_M)
        else:
            minute = 60*(out_H-in_H-1) + (60+out_M-in_M)
        return minute
    
    def fee(m):
        if fees[0] >= m:
            tot = fees[1]
        else:
            tot = fees[1] + ((m-fees[0])//fees[2]) * fees[3] 
            if (m-fees[0])%fees[2]:
                tot += fees[3]
        return tot
    
    answer = []
    numbers = {}
    check = {}
    for record in records:
        time, num, state = record.split()
        if state == 'IN':
            check[num] = time
        elif state == 'OUT':
            if num in numbers:
                numbers[num] += hour(check[num], time)
                del(check[num])
            else:
                numbers[num] = hour(check[num], time)
                del(check[num])

    for i in check.keys():
        if i in numbers:
            numbers[i] += hour(check[i], '23:59')
        else:
            numbers[i] = hour(check[i], '23:59')

    lst = []
    for num in numbers:
        lst.append([int(num), fee(numbers[num])])

    lst.sort()
    for i in range(len(lst)):
        answer.append(lst[i][1])
        
    return answer

'''
테스트 1 〉통과 (0.07ms, 10.5MB)
테스트 2 〉통과 (0.03ms, 10.5MB)
테스트 3 〉통과 (0.08ms, 10.4MB)
테스트 4 〉통과 (0.08ms, 10.4MB)
테스트 5 〉통과 (0.24ms, 10.4MB)
테스트 6 〉통과 (0.48ms, 10.4MB)
테스트 7 〉통과 (1.91ms, 10.4MB)
테스트 8 〉통과 (0.91ms, 10.4MB)
테스트 9 〉통과 (0.33ms, 10.3MB)
테스트 10 〉통과 (2.80ms, 10.4MB)
테스트 11 〉통과 (3.12ms, 10.8MB)
테스트 12 〉통과 (2.50ms, 10.7MB)
테스트 13 〉통과 (0.04ms, 10.4MB)
테스트 14 〉통과 (0.05ms, 10.6MB)
테스트 15 〉통과 (0.03ms, 10.6MB)
테스트 16 〉통과 (0.04ms, 10.4MB)
'''