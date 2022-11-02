import math

def solution(fees, records):
    answer = []
    parking = dict()
    total = dict()

    for record in records:
        time, number, inout = record.split()
        if inout == 'IN':
            parking[number] = time
        else:
            car_in = int(parking[number][0:2]) * 60 + int(parking[number][3:])
            car_out = int(time[0:2]) * 60 + int(time[3:])
            parking.pop(number)
            if number not in total:
                total[number] = car_out - car_in
            else:
                total[number] = total[number] + car_out - car_in

    if parking:
        for key, value in parking.items():
            if key in total:
                total[key] = total[key] + 1439 - (int(value[0:2]) * 60 + int(value[3:]))
            else:
                total[key] = 1439 - (int(value[0:2]) * 60 + int(value[3:]))

    total = sorted(total.items())

    for number, time in total:
        fee = fees[1]
        time -= fees[0]
        if time > 0:
            fee += math.ceil(time / fees[2]) * fees[3]

        answer.append(fee)

    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))

'''
테스트 1 〉	통과 (0.04ms, 10.5MB)
테스트 2 〉	통과 (0.04ms, 10.4MB)
테스트 3 〉	통과 (0.05ms, 10.4MB)
테스트 4 〉	통과 (0.07ms, 10.4MB)
테스트 5 〉	통과 (0.13ms, 10.4MB)
테스트 6 〉	통과 (0.15ms, 10.5MB)
테스트 7 〉	통과 (1.29ms, 10.6MB)
테스트 8 〉	통과 (0.76ms, 10.5MB)
테스트 9 〉	통과 (0.15ms, 10.4MB)
테스트 10 〉	통과 (1.07ms, 10.5MB)
테스트 11 〉	통과 (1.45ms, 10.5MB)
테스트 12 〉	통과 (1.55ms, 10.7MB)
테스트 13 〉	통과 (0.04ms, 10.3MB)
테스트 14 〉	통과 (0.03ms, 10.4MB)
테스트 15 〉	통과 (0.03ms, 10.4MB)
테스트 16 〉	통과 (0.02ms, 10.4MB)
'''