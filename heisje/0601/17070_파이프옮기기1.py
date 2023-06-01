class Move:

  def row(r2, c2):
      return ((0, r2, c2+1), (2, r2+1, c2+1))
      
  def col(r2, c2):
      return [(1, r2+1, c2), (2, r2+1, c2+1)]
      
  def dia(r2, c2):
      return [(1, r2+1, c2), (2, r2+1, c2+1), (0, r2, c2+1)]
  
  move = {
      0:row,
      1:col,
      2:dia,
  }

  def getR2C2(self, type, r2, c2):
      return self.move[type](r2, c2)
  
def main(N, grid):
    answerGrid = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
    answerGrid[0][1][0] = 1

    move = Move()
    for r in range(N):
        for c in range(1, N):
            for bType, cnt in enumerate(answerGrid[r][c]):
                if cnt > 0:
                    for type, newR2, newC2 in move.getR2C2(bType, r, c):
                        if newR2 < N and newC2 < N:
                            if grid[newR2][newC2] == 0:
                                # 대각선일 때 제외사항
                                if type == 2 and (grid[newR2 - 1][newC2] == 1 or grid[newR2][newC2 - 1] == 1):
                                    continue
                                answerGrid[newR2][newC2][type] += answerGrid[r][c][bType]
        
    # 도착이면
    print(sum(answerGrid[N-1][N-1]))

N = int(input())
Grid = [list(map(int, input().split())) for _ in range(N)]
main(N, Grid)