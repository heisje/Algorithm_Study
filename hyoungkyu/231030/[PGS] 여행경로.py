# Lv3
def solution(tickets):
    answer = []
    tickets.sort()
    
    visited = [0] * len(tickets)
    flag = False
    
    # "ICN" 시작이 여러 개인 경우 다 돌려야됨
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            idx = i
            visited[idx] = 1
            answer = dfs(tickets, visited, idx, len(tickets)-1, ["ICN"])
            # 티켓을 다 쓰고 경로를 찾았을 경우
            if len(answer) == len(tickets)+1:
                return answer
            # "ICN"으로 시작하는 티켓을 찾은 경우
            flag = True
            # 티켓 초기화
            visited[idx] = 0
        # "ICN"으로 시작하는 티켓을 지나친 경우 break
        elif flag:
            break
            
    return answer

def dfs(tickets, visited, idx, cnt, plan):
    # 여행지 경로 배열 deepcopy
    tmp_plan = plan[:]
    # 여행지를 다 찾은 경우
    if cnt == 0:
        tmp_plan.append(tickets[idx][1])
        return tmp_plan
    # 전체 티켓 순환
    for i in range(len(tickets)):
        # 여행갈 수 있는 경우
        if not visited[i] and tickets[idx][1] == tickets[i][0]:
            visited[i] = 1
            # 재귀
            tmp_plan = dfs(tickets, visited, i, cnt-1, plan + [tickets[i][0]])
            # 여행 경로를 완성한 경우
            if len(tmp_plan) == len(tickets) + 1:
                return tmp_plan
            visited[i] = 0
    # 여행 경로를 못찾은 경우
    return tmp_plan
    
'''
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
'''