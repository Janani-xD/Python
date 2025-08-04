from collections import deque
class binaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert_node(root, data):
    if root is None:
        return binaryTree(data)
    queue = deque([root])

    while queue:
        temp = queue.popleft()

        if temp.left is None:
            temp.left = binaryTree(data)
            break
        else:
            queue.append(temp.left)
        if temp.right is None:
            temp.right = binaryTree(data)
            break
        else:
            queue.append(temp.right)
    return root

def delete_node(self, Node, data):
    if Node is None:
        return
    queue = deque([Node])
    target = None
    while queue:
        temp = queue.popleft()
        if temp.data == data:
            target = temp
            break
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)

    if target is None:
        return Node

    last_node = None
    last_parent = None
    queue = deque([(Node, None)])

    while queue:
        curr, parent = queue.popleft()
        last_node = curr
        last_parent = parent

        if curr.left:
            queue.append((curr.left, curr))
        if curr.right:
            queue.append((curr.right,curr))
        target.data = last_node.data

        if last_parent:
            if last_parent.left == last_node:
                last_parent.left = None
            else:
                last_parent.right = None
        else:
            return None
        return Node



def pre_order_traversal(Node):
    if Node is None:
        return
    print(" data in pre - order : ", Node.data)
    pre_order_traversal(Node.left)
    pre_order_traversal(Node.right)

def in_order_traversal(Node):
    if Node is None:
        return
    in_order_traversal(Node.left)
    print(" data in in - order : ", Node.data)
    in_order_traversal(Node.right)

def post_order_traversal(Node):
    if Node is None:
        return
    post_order_traversal(Node.left)
    post_order_traversal(Node.right)
    print(" data in post - order : ", Node.data)

#level order traversal
def bfs(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.pop(0)
        print(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


node1 = binaryTree(2)
node2 = binaryTree(3)
node3 = binaryTree(4)
node4 = binaryTree(5)

node1.left = node2
node1.right = node3

node2.left = node4

print(node1.data)
print(node1.left.data)
print(node1.left.left.data)
print(node1.right.data)
insert_node(node1, 10)
print(pre_order_traversal(node1))
print(in_order_traversal(node1))
print(post_order_traversal(node1))
