def solution(fees, records):
    answer = []
    base_time = fees[0]
    base_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]

    cars = {}

    for i in range(len(records)):
        data = list(records[i].split())
        try:
            cars[data[1]].append(int(data[0][0]+data[0][1])*60 + int(data[0][3]+data[0][4]))
        except KeyError:
            cars[data[1]] = [int(data[0][0]+data[0][1])*60 + int(data[0][3]+data[0][4])]

    car_list = list(cars.keys())
    car_list.sort()
    for car in car_list:
        pay_to = 0
        total_time = 0
        if len(cars[car]) % 2:
            cars[car].append(23*60 + 59)
        for i in range(len(cars[car])//2):
            total_time += cars[car][2*i + 1] - cars[car][2*i]

        if total_time - base_time <= 0:
            pay_to = base_fee
        else:
            pay_to = base_fee
            rest_time_to_pay = total_time - base_time
            pay_to += (rest_time_to_pay // unit_time) * unit_fee
            if rest_time_to_pay % unit_time:
                pay_to += unit_fee
        answer.append(pay_to)
    return answer