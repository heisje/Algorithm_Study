"""
def down(resultList, count, current):
    new_current = current

    while(count > 0):
        if resultList[new_current + 1] == "O":
            count -= 1
        new_current += 1

    return new_current


def up(resultList, count, current):
    new_current = current

    while(count > 0):
        if resultList[new_current - 1] == "O":
            count -= 1
        new_current -= 1

    return new_current


def del_row(resultList, current, lastIndex, deletedStack):
    new_current = current
    resultList[current] = "X"
    deletedStack.append(current)

    if current == lastIndex:

        temp = lastIndex
        while(True):
            temp -= 1
            if resultList[temp] == "O":
                lastIndex = temp
                new_current = temp
                break
            else:
                continue
    else:

        temp = current
        while(True):
            temp += 1
            if resultList[temp] == "O":
                new_current = temp
                break
            else:
                continue

    return new_current, lastIndex

def cancel(resultList, deletedStack, current):
    temp = deletedStack.pop()
    resultList[temp] = "O"


def solution(n, k, cmd):
    answer = ''

    result_list = ["O" for i in range(n)]
    deleted_stack = []  # 스택

    # total_len = n
    last_idx = n - 1

    cur = k

    for i in range(len(cmd)):
        if cmd[i][0] == "D":
            cur = down(result_list, int(cmd[i][2]), cur)

        elif cmd[i][0] == "U":
            cur = up(result_list, int(cmd[i][2]), cur)

        elif cmd[i][0] == "C":
            cur, last_idx = del_row(result_list, cur, last_idx, deleted_stack)
            # total_len -= 1

        elif cmd[i][0] == "Z":
            cancel(result_list, deleted_stack, cur)


    # print(result_list)
    answer_str = ''.join(result_list)
    # print(answer_str)
    return answer_str


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))

# 클래스로 다시 풀어보자

"""
class Node :
    def __init__(self,left = None,right = None):
        self.remove = False
        self.left = left
        self.right = right

def solution(n, k, cmd):
    # linked -list
    table = [Node(i-1,i+1) for i in range(n)]
    table[0].left= None
    table[n - 1].right = None
    cursor = k
    stack = []
    for i in cmd:
        if i[0] == 'U':
            pos, move = i.split()
            for _ in range(int(move)):
                cursor = table[cursor].left
        elif i[0] == 'D':
            pos,move = i.split()
            for _ in range(int(move)):
                cursor = table[cursor].right
        elif i[0] == 'C':
            stack.append(cursor)
            table[cursor].remove = True

            l,r = table[cursor].left , table[cursor].right

            if l or l == 0:
                table[l].right = r
            # 마지막행이면
            if r:
                table[r].left = l
                cursor = r
            else:
                cursor = l
        else:
            c = stack.pop()
            table[c].remove = False

            l,r = table[c].left,table[c].right
            # 복원된 행이 첫째행이아니라면
            if l:
                table[l].right =c
            if r:
                table[r].left = c

    answer = ""
    for i in range(n):
        if table[i].remove :
            answer += "X"
        else:
            answer += "O"
    return answer
