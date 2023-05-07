class TableCmd:
    def __init__(self, n: int, k: int):
        self.n = n
        self.k = k
        self.table = {i for i in range(n)}
        self.stack = []

    def upward(self, x):
        self.k -= x

    def downward(self, x):
        self.k += x

    def delete(self):
        lst_tbl = list(self.table)
        print(lst_tbl, type(lst_tbl))
        d = lst_tbl[self.k]
        self.table.remove(d)
        self.stack.append(d)
        # 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
        if self.k == len(self.table):
            self.k -= 1

    def undo(self):
        # 단, 현재 선택된 행은 바뀌지 않습니다.
        lst_tbl = list(self.table)
        now = lst_tbl[self.k]
        d = self.stack.pop()
        self.table.add(d)
        self.k = list(self.table).index(now)

    def compare(self):
        result = ''
        for i in range(self.n):
            if i in self.table:
                result += 'O'
            else:
                result += 'X'
        return result


def solution(n, k, cmd):
    process = TableCmd(n, k)
    for c in cmd:
        first = c[0]
        if first == "U":
            process.upward(int(c[-1]))
        elif first == "D":
            process.downward(int(c[-1]))
        elif first == "C":
            process.delete()
        elif first == "Z":
            process.undo()

    return process.compare()

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))