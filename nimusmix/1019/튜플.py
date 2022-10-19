def solution(s):
    s = s.strip('{').strip('}').split('},{')
    tmp = [0] * 1000001
    answer = []
    
    for x in s:
        t = x.split(',')
        for y in t:
            tmp[int(y)] += 1
    
    for idx, i in enumerate(tmp):
        if i:
            answer.append((i, idx))
    
    answer.sort(reverse=True)
    answer = list(map(lambda x:x[1], answer))
    return answer