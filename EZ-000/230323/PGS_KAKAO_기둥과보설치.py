class ColumnAndBeam:
    def erect_column(self, x, y, answer):
        c1 = (y == 0)
        c2 = (x - 1, y, 1) in answer
        c3 = (x, y, 1) in answer
        c4 = (x, y - 1, 0) in answer
        if c1 or c2 or c3 or c4:
            answer.add((x, y, 0))

    def erect_beam(self, x, y, answer):
        c1 = (x, y - 1, 0) in answer
        c2 = (x + 1, y - 1, 0) in answer
        c3 = (x - 1, y, 1) in answer and (x + 1, y, 1) in answer
        if c1 or c2 or c3:
            answer.add((x, y, 1))

    def check_column(self, x, y, answer):
        if (x, y, 0) in answer:
            c1 = (y == 0)
            c2 = (x - 1, y, 1) in answer
            c3 = (x, y, 1) in answer
            c4 = (x, y - 1, 0) in answer
            if c1 or c2 or c3 or c4:
                return True
            return False
        return True

    def check_beam(self, x, y, answer):
        if (x, y, 1) in answer:
            c1 = (x, y - 1, 0) in answer
            c2 = (x + 1, y - 1, 0) in answer
            c3 = (x - 1, y, 1) in answer and (x + 1, y, 1) in answer
            if c1 or c2 or c3:
                return True
            return False
        return True

    def remove_column(self, x, y, answer):
        answer.remove((x, y, 0))
        if not (self.check_column(x, y + 1, answer) and self.check_beam(x - 1, y + 1, answer) and self.check_beam(x, y + 1, answer)):
            answer.add((x, y, 0))

    def remove_beam(self, x, y, answer):
        answer.remove((x, y, 1))
        if self.check_column(x, y, answer) and self.check_column(x + 1, y, answer) and self.check_beam(x - 1, y, answer) and self.check_beam(x, y, answer):
            answer.add((x, y, 1))


def solution(n, build_frame):
    # 기둥, 보 = 0, 1 / 삭제, 설치 = 0, 1
    answer = set()
    building = ColumnAndBeam()
    for frame in build_frame:
        x, y, a, b = frame
        if not a and not b:
            building.remove_column(x, y, answer)
        elif not a and b:
            building.erect_column(x, y, answer)
        elif a and not b:
            building.remove_beam(x, y, answer)
        elif a and b:
            building.erect_beam(x, y, answer)

    answer = sorted(list(map(list, answer)), key=lambda e: (e[0], e[1], e[2]))
    return answer

build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(5, build_frame))
