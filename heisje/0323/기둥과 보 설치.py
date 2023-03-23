def solution(n, build_frame):
    board = [[[False for _ in range(2)] for _ in range(n+1)] for _ in range(n+1)]
    
    def col_check(x, y):
        if y == 0:
            return True
        
        if 0<=x<=n and 0<=y<=n and board[x][y][1]:
            return True
        if 0<=x-1<=n and 0<=y<=n and board[x-1][y][1]:
            return True
        if 0<=x<=n and 0<=y-1<=n and board[x][y-1][0]:
            return True
        
        return False
    
    def bo_check(x,y):
        if 0<=x-1<=n and 0<=y<=n and board[x-1][y][1]:
            if 0<=x+1<=n and 0<=y<=n and board[x+1][y][1]:
                return True
        
        if (0<=x+1<=n and 0<=y-1<=n and board[x+1][y-1][0]) or (0<=x<=n and 0<=y-1<=n and board[x][y-1][0]):
                return True
        

        return False

    for x, y, a, b in build_frame:
        if b == 0: # delete      
            if a == 0: # column
                board[x][y][0] = False
                
 
                possible = True
                for i in range(n+1):
                    for j in range(n+1):
                        if board[i][j][0] and not col_check(i,j):
                            possible = False
                        if board[i][j][1] and not bo_check(i,j):
                            possible = False

                    
                if not possible:
                    board[x][y][0] = True

            else : # bo
                board[x][y][1] = False
                
                possible = True
                for i in range(n+1):
                    for j in range(n+1):
                        if board[i][j][0] and not col_check(i,j):
                            possible = False
                        if board[i][j][1] and not bo_check(i,j):
                            possible = False

                if not possible:
                    board[x][y][1] = True
                
        else: # setup
            
            if a == 0: # column
                if col_check(x,y):
                    board[x][y][0] = True
            else : # bo
                if bo_check(x,y):
                    board[x][y][1] = True
    
    answer = []
    
    for i in range(n+1):
        for j in range(n+1):
            for k in range(2):
                if board[i][j][k]:
                    answer.append([i,j,k])
    
    
    return answer


# class Building:
    
#     def __init__(this, n):
#         this.bos = [[0 for _ in range(n+1)] for _ in range(n+1)]
#         this.pis = [[0 for _ in range(n+1)] for _ in range(n+1)]
#         this.n = n+1
#     # 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 
#         # 또는 다른 기둥 위에 있는지 판별
#     # 보는 한쪽 끝 부분이 기둥 위에 있거나, 
#         # 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
#     def createBo(this, x, y):
#         if this.pis[y-1][x] == 1:     # 기둥이 왼쪽에 있을 때 보
#             this.bos[y][x] = 1
#         elif 0 <= x+1 < this.n and  0 <= y-1 < this.n \
#             and this.pis[y-1][x+1] == 1:     # 기둥이 오른쪽에 있을 때 보
#             this.bos[y][x] = 1
#         elif this.bos[y][x-1] == 1 and this.bos[y][x+1] == 1: # 다른 보가 있으면 보
#             this.bos[y][x] = 1
#     def createPi(this, x, y):
#         if y == 0:                      # 바닥 위
#             this.pis[y][x] = 1
#         elif this.pis[y-1][x] == 1: # 다른 기둥 위에 있거나
#             this.pis[y][x] = 1
#         elif this.bos[y][x-1] == 1 : # 오른쪽 보 위에있는 경우
#             if x - 1 == this.n - 1: # 오른쪽 끝인 경우 제작
#                 this.pis[y][x] = 1
#             elif 0 <= x+1 < this.n and this.bos[y][x+1] == 0: # 오른쪽이 0이면 제작
#                 this.pis[y][x] = 1
#         elif this.bos[y][x] == 1 : # 왼쪽 보 위에있는 경우
#             if x == 0: # 왼쪽 끝인 경우 제작
#                 this.pis[y][x] = 1
#             elif 0 <= x - 1 < this.n and this.bos[y][x-1] == 0: # 왼쪽이 0이면 제작
#                 this.pis[y][x] = 1
#     def deleteBo(this, x, y):
#         this.bos[y][x] = 0
#         # 보를 삭제했는데, 
        
#     def deletePi(this, x, y):
#         pass
#     def check(this):
#         pass
                
# def solution(n, build_frame):
#     answer = [[]]
    
#     building = Building(n)
    
#     for build in build_frame:
#         x, y, a, b = build
#         try:
#             if a: # 보
#                 if b:                   # 삭제
#                     building.createBo(x, y)
#                 else:                   # 생성
#                     building.deleteBo(x, y)
#             else:
#                 if b:                   # 삭제
#                     building.createPi(x, y)
#                 else:                   # 생성
#                     building.deletePi(x, y)
#         except:
#             pass
        
#     print(building.pis)
#     print(building.bos)
    
#     return answer