class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def is_complete_binary_tree(root):
    if not root:
        return True

    # 노드의 번호를 순서대로 부여하기 위한 리스트
    nodes = [root]

    while nodes:
        current = nodes.pop(0)  # 리스트에서 첫 번째 노드를 꺼냄

        if current:
            nodes.append(current.left)  # 현재 노드의 왼쪽 자식을 리스트에 추가
            nodes.append(current.right)  # 현재 노드의 오른쪽 자식을 리스트에 추가
        else:
            # 만약 None(비어있는 자리)이 나오면, 그 뒤에 나와야 할 모든 노드는 None이어야 함
            for node in nodes:
                if node:
                    return False

    return True

# 주어진 구조의 이진 트리
c = TNode('C', None, None)
d = TNode('D', None, None)
b = TNode('B', c, d)
f = TNode('F', None, None)
e = TNode('E', None, f)
root = TNode('A', b, e)

print(is_complete_binary_tree(root))