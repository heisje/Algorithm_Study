# Lv3 / hash를 이용한 방문체크 처음 해봄, 회전 조건에서 0<ti-1, 0<tj-1 이렇게 삽질해서 오래 걸림 (원래는 <=)
from collections import deque

def solution(board):
    answer = bfs(board)
    return answer

def bfs(board):
    n = len(board)
    que = deque()
    que.append([(0, 0), (0, 1)])
    visited_dic = {}
    visited_dic['0,0,0,1'] = 0
    
    while que:
        cpos_0, cpos_1 = que.popleft()
        ci_0, cj_0 = cpos_0
        ci_1, cj_1 = cpos_1
        cost = visited_dic[f'{ci_0},{cj_0},{ci_1},{cj_1}']
        # 종료 조건
        if (ci_0 == n-1 and cj_0 == n-1) or (ci_1 == n-1 and cj_1 == n-1):
            return cost
        
        # 형태 그대로 이동하는 경우 (상하좌우)
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni_0, nj_0 = ci_0+di, cj_0+dj
            ni_1, nj_1 = ci_1+di, cj_1+dj
            if 0<=ni_0<n and 0<=nj_0<n and 0<=ni_1<n and 0<=nj_1<n and not board[ni_0][nj_0] and not board[ni_1][nj_1]:
                append_que(que, [(ni_0, nj_0), (ni_1, nj_1)], cost, visited_dic)
        
        # 회전하는 경우
        rotate(board, [(ci_0, cj_0), (ci_1, cj_1)], visited_dic, que, cost)
        
def rotate(board, pos, visited_dic, que, cost):
    n = len(board)
    flag = check_pos(pos[0], pos[1])    # True - 가로방향, False - 세로방향
    if flag:
        ti, tj = pos[0][0], pos[0][1]   # 축
        # 오른쪽 아래로 회전
        if ti+1 < n and not board[ti+1][tj+1] and not board[ti+1][tj]:
            append_que(que, [(ti, tj), (ti+1, tj)], cost, visited_dic)
        # 오른쪽 위로 회전
        if 0 <= ti-1 and not board[ti-1][tj] and not board[ti-1][tj+1]:
            append_que(que, [(ti, tj), (ti-1, tj)], cost, visited_dic)
            
        ti, tj = pos[1][0], pos[1][1]   # 축
        # 왼쪽 아래로 회전
        if ti+1 < n and not board[ti+1][tj-1] and not board[ti+1][tj]:
            append_que(que, [(ti, tj), (ti+1, tj)], cost, visited_dic)
        # 왼쪽 위로 회전
        if 0 <= ti-1 and not board[ti-1][tj-1] and not board[ti-1][tj]:
            append_que(que, [(ti, tj), (ti-1, tj)], cost, visited_dic)
    
    else:
        ti, tj = pos[1][0], pos[1][1]   # 축
        # 위쪽 우측으로 회전
        if tj+1 < n and not board[ti-1][tj+1] and not board[ti][tj+1]:
            append_que(que, [(ti, tj), (ti, tj+1)], cost, visited_dic)
        # 위쪽 좌측으로 회전
        if 0 <= tj-1 and not board[ti-1][tj-1] and not board[ti][tj-1]:
            append_que(que, [(ti, tj), (ti, tj-1)], cost, visited_dic)
            
        ti, tj = pos[0][0], pos[0][1]   # 축
        # 아래쪽 우측으로 회전
        if tj+1 < n and not board[ti+1][tj+1] and not board[ti][tj+1]:
            append_que(que, [(ti, tj), (ti, tj+1)], cost, visited_dic)
        # 야래쪽 좌측으로 회전
        if 0 <= tj-1 and not board[ti+1][tj-1] and not board[ti][tj-1]:
            append_que(que, [(ti, tj), (ti, tj-1)], cost, visited_dic)
            
def check_pos(pos_0, pos_1):
    if pos_0[0] - pos_1[0] == 0:
        return True # 가로
    return False    # 세로

def append_que(que, pos, cost, visited_dic):
    pos.sort()
    pos_1, pos_2 = pos
    if f'{pos_1[0]},{pos_1[1]},{pos_2[0]},{pos_2[1]}' in visited_dic:
        return    
    visited_dic[f'{pos_1[0]},{pos_1[1]},{pos_2[0]},{pos_2[1]}'] = cost + 1
    que.append([pos_1, pos_2])

'''
정확성  테스트
테스트 1 〉	통과 (0.13ms, 10.3MB)
테스트 2 〉	통과 (0.15ms, 10.3MB)
테스트 3 〉	통과 (0.14ms, 10.4MB)
테스트 4 〉	통과 (0.58ms, 10.1MB)
테스트 5 〉	통과 (0.46ms, 10.1MB)
테스트 6 〉	통과 (0.70ms, 10.3MB)
테스트 7 〉	통과 (1.97ms, 10.4MB)
테스트 8 〉	통과 (2.74ms, 10.3MB)
테스트 9 〉	통과 (2.72ms, 10.3MB)
테스트 10 〉	통과 (2.51ms, 10.2MB)
테스트 11 〉	통과 (1.63ms, 10.2MB)
테스트 12 〉	통과 (1.78ms, 10.3MB)
테스트 13 〉	통과 (66.00ms, 11MB)
테스트 14 〉	통과 (35.62ms, 10.6MB)
'''