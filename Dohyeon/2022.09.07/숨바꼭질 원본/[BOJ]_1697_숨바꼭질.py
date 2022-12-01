subin, bro = map(int, input().split())

now = subin
target = bro

count = 0

while(now != target):
    if now == 0:
        now += 1
        count += 1
        continue

    if target < now:
        count = count + now - count
        now = target

    elif target == now * 2:
        count = count + 1
        now = target

    elif target == now * 2 + 1 or target == now * 2 - 1:
        count = count + 2
        now = target

    elif target > now * 2:
        if now % 2:                     # 현재 홀수일 때
            if target // 2 > (now // 2 + 1):
                now = now * 2
                count = count + 1
                continue
            else:
                min_plus = 1
                while(True):
                    if (now + min_plus)*2 > target:
                        min_plus = min_plus - 1
                        break
                    else:
                        min_plus = min_plus + 1
                count = count + min_plus
                count += 1
                count = count + target - (now + min_plus) * 2
                break
        else:                           # 현재 짝수일 때
            if target // 2 > (now // 2):
                now = now * 2
                count = count + 1
                continue
            else:
                min_plus = 1
                while(True):
                    if (now + min_plus)*2 > target:
                        min_plus = min_plus - 1
                        break
                    else:
                        min_plus = min_plus + 1
                count = count + min_plus
                count += 1
                count = count + target - (now + min_plus) * 2
                break
    elif target < now * 2:
        if now % 2:
            if target <= now + (now // 2):
                count = count + target - now
            else:
                min_count = target
                for i in range(1, now // 2):
                    temp = i + 1 + abs(target - (now - i) * 2)
                    if temp < min_count:
                        min_count = temp

                count = count + min_count

                break
        else:
            if target < now + (now // 2):
                count = count + target - now
            else:
                min_count = target
                for i in range(1, now // 2):
                    temp = i + 1 + abs(target - (now - i) * 2)
                    if temp < min_count:
                        min_count = temp

                count = count + min_count

                break



print(count)