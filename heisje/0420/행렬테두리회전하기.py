def solution(rows, columns, queries):
    answer = []
    table = list([1 + x + y * columns for x in range(columns)] for y in range(rows))
    for query in queries:
        # query  = [startX, startY, endX, endY]
        query = [x-1 for x in query] # 0부터 시작하는 인덱스에 맞춰 1씩 빼줌
        tmp = table[query[0]][query[1]] # 왼쪽 위 값 저장
        small = tmp
        
        # left 첫재칸 제외
        for i in range(query[0]+1, query[2]+1):
            table[i-1][query[1]] = table[i][query[1]]
            small = min(small, table[i][query[1]])
        # bottom
        for i in range(query[1]+1, query[3]+1):
            table[query[2]][i-1] = table[query[2]][i]
            small = min(small, table[query[2]][i])
        # right
        for i in range(query[2]-1, query[0]-1, -1):
            table[i+1][query[3]] = table[i][query[3]]
            small = min(small, table[i][query[3]])
        # top
        for i in range(query[3]-1, query[1]-1, -1):
            table[query[0]][i+1] = table[query[0]][i]
            small = min(small, table[query[0]][i])
        table[query[0]][query[1]+1] = tmp
        
        answer.append(small)    
    return answer
# 테스트 1 〉	통과 (0.04ms, 10.3MB)
# 테스트 2 〉	통과 (0.05ms, 10.3MB)
# 테스트 3 〉	통과 (276.47ms, 11.7MB)
# 테스트 4 〉	통과 (149.18ms, 11.3MB)
# 테스트 5 〉	통과 (217.41ms, 11.5MB)
# 테스트 6 〉	통과 (222.70ms, 11.9MB)
# 테스트 7 〉	통과 (238.83ms, 12.1MB)
# 테스트 8 〉	통과 (143.19ms, 11.3MB)
# 테스트 9 〉	통과 (203.77ms, 12MB)
# 테스트 10 〉	통과 (191.50ms, 11.6MB)
# 테스트 11 〉	통과 (181.07ms, 11.4MB)

