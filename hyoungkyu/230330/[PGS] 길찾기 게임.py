import sys
sys.setrecursionlimit(10**6)

# data = [value, x, y]
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        
class BinaryTree(list):
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None
    
    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data[0] < node.data[0]:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node
    
    def pre_order_traversal(self):
        res = []
        def _pre_order_traversal(root):
            if root is None:
                pass
            else:
                if root is not None:
                    res.append(root.data[2])
                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)
                return res
        return _pre_order_traversal(self.root)
    
    def post_order_traversal(self):
        res = []
        def _post_order_traversal(root):
            if root is None:
                pass
            else:
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                if root is not None:
                    res.append(root.data[2])
                return res
        return _post_order_traversal(self.root)

                

def solution(nodeinfo):
    answer = []
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    nodeinfo.sort(key = lambda x : x[1], reverse=True)
    
    tree = BinaryTree()
    for node in nodeinfo:
        tree.insert(node)
        
    answer.append(tree.pre_order_traversal())
    answer.append(tree.post_order_traversal())
    
    return answer

'''
테스트 1 〉	통과 (0.03ms, 10.1MB)
테스트 2 〉	통과 (0.04ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.4MB)
테스트 6 〉	통과 (116.40ms, 11.3MB)
테스트 7 〉	통과 (128.94ms, 11.3MB)
테스트 8 〉	통과 (68.34ms, 12MB)
테스트 9 〉	통과 (394.24ms, 14.7MB)
테스트 10 〉	통과 (20.47ms, 10.8MB)
테스트 11 〉	통과 (308.03ms, 14.6MB)
테스트 12 〉	통과 (369.32ms, 14.6MB)
테스트 13 〉	통과 (0.47ms, 10.2MB)
테스트 14 〉	통과 (7.15ms, 10.6MB)
테스트 15 〉	통과 (30.69ms, 12.2MB)
테스트 16 〉	통과 (58.08ms, 14.4MB)
테스트 17 〉	통과 (4.21ms, 10.6MB)
테스트 18 〉	통과 (58.81ms, 13.8MB)
테스트 19 〉	통과 (14.75ms, 10.9MB)
테스트 20 〉	통과 (21.88ms, 12MB)
테스트 21 〉	통과 (35.68ms, 12.6MB)
테스트 22 〉	통과 (57.65ms, 14.1MB)
테스트 23 〉	통과 (60.51ms, 14.3MB)
테스트 24 〉	통과 (0.04ms, 10.3MB)
테스트 25 〉	통과 (0.03ms, 10.4MB)
테스트 26 〉	통과 (215.29ms, 11.7MB)
테스트 27 〉	통과 (0.03ms, 10.2MB)
테스트 28 〉	통과 (0.08ms, 10.2MB)
테스트 29 〉	통과 (0.01ms, 10.1MB)
'''