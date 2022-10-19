def solution(s):
    arr = []
    for a in s.strip('{').strip('}').split('},{'):
        arr.append(list(map(int,a.split(','))))
        
    arr.sort(key=lambda x:len(x))    
    answer = []
    for a in arr:
        for aa in set(a):
            if aa not in answer:
                answer.append(aa)
    
    return answer