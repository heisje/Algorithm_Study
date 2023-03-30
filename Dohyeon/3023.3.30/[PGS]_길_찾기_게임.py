import sys
sys.setrecursionlimit(10**6)

data_dict = {}              # y 값이 key값, [x, 인덱스] 를 value값
pre_list = []
post_list = []

class Node:
    my_self = None
    left = None
    right = None
    parent = None

    x = None
    y = None

    def __init__(self, my_self, x, y):
        self.my_self = my_self
        self.x = x
        self.y = y


def pre(base_node):
    if base_node == None:
        return
    pre_list.append(base_node.my_self)
    pre(base_node.left)
    pre(base_node.right)

def post(base_node):
    if base_node == None:
        return
    post(base_node.left)
    post(base_node.right)
    post_list.append(base_node.my_self)


def make_tree(root_node, keyList):   # 부모가 될 노드, 현재 keylist의 인덱스, keylist

    for i in range(len(keyList)):
        if i == 0:      # 루트노드
            continue
        for j in range(len(data_dict[keyList[i]])):
            new_node = data_dict[keyList[i]][j][1]
            found = False
            target = root_node
            while(not found):

                if target.x > new_node.x:     # 왼쪽 분기
                    if target.left != None:
                        target = target.left                # 이미 노드가있으면 다음
                    else:
                        target.left = new_node  # 노드 없으면 자리잡자
                        found = True
                else:                                       # 오른쪽 분기
                    if target.right != None:
                        target = target.right
                    else:
                        target.right = new_node
                        found = True

#     return

    # if parent_node == None:
    #     return
    #
    # grand_x_left = -1
    # grand_x_right = 100001
    #
    # if parent_node.parent != None:
    #     if parent_node.x > parent_node.parent.x:    # 오른쪽으로 분기된 부모
    #         grand_x_left = parent_node.parent.x
    #     else:                                       # 왼쪽으로 분기된 부모
    #         grand_x_right = parent_node.parent.x
    #
    # before_node = None
    #
    # if idx + 1 == len(keyList): # 더이상 아래가 없음
    #     return
    #
    # for x, node in data_dict[keyList[idx + 1]]:
    #     if x > parent_node.x:
    #
    #         if x < grand_x_right:
    #             parent_node.right = node
    #             node.parent = parent_node
    #
    #         if before_node != None:
    #             if grand_x_left < before_node.x:
    #                 parent_node.left = before_node
    #                 before_node.parent = parent_node
    #
    #         break
    #
    #     else:
    #         before_node = node
    #
    # else:
    #     if before_node != None:
    #         if grand_x_left < before_node.x:
    #             parent_node.left = before_node
    #             before_node.parent = parent_node
    #
    #
    # make_tree(parent_node.left, idx + 1, keyList)
    # make_tree(parent_node.right, idx + 1, keyList)

def solution(nodeinfo):
    top = 0

    for i in range(len(nodeinfo)):
        try:
            data_dict[nodeinfo[i][1]].append([nodeinfo[i][0], Node(i + 1, nodeinfo[i][0], nodeinfo[i][1])])
        except KeyError:
            data_dict[nodeinfo[i][1]] = [[nodeinfo[i][0], Node(i + 1, nodeinfo[i][0], nodeinfo[i][1])]]
        if top < nodeinfo[i][1]:
            top = nodeinfo[i][1]

    key_list = list(data_dict.keys())
    key_list.sort(reverse=True)
    # for i in range(len(key_list)):
    #     data_dict[key_list[i]].sort()         # 각 층 마다 x좌표 기준으로 정렬

    make_tree(data_dict[top][0][1], key_list)
    answer = []

    # for i in range(len(key_list)):
    #     for j in range(len(data_dict[key_list[i]])):
    #         print(data_dict[key_list[i]][j][1].my_self, end="")
    #         print("노드의 부모 노드 : ")
    #         if data_dict[key_list[i]][j][1].parent != None:
    #             print(data_dict[key_list[i]][j][1].parent.my_self)
    #
    #         else:
    #             print(None)
    #
    #         print(data_dict[key_list[i]][j][1].my_self, end="")
    #         print("노드의 왼쪽 자식 노드 : ")
    #         if data_dict[key_list[i]][j][1].left != None:
    #             print(data_dict[key_list[i]][j][1].left.my_self)
    #         else:
    #             print(None)
    #
    #         print(data_dict[key_list[i]][j][1].my_self, end="")
    #         print("노드의 오른쪽 자식 노드 : ")
    #         if data_dict[key_list[i]][j][1].right != None:
    #             print(data_dict[key_list[i]][j][1].right.my_self)
    #         else:
    #             print(None)


    pre(data_dict[top][0][1])
    post(data_dict[top][0][1])

    answer.append(pre_list)
    answer.append(post_list)
    return answer