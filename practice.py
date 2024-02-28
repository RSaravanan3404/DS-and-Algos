def inOrder(node):
    if node is None:
        return 
    inOrder(node.left)
    print(node.data, end=' ')
    inOrder(node.right)

def preOrder(node):
    if node is None:
        return 
    print(node.data, end=' ')
    preOrder(node.left)
    preOrder(node.right)

def postOrder(node):
    if node is None:
        return 
    postOrder(node.left)
    postOrder(node.right)
    print(node.data, end=' ')



def height(root):
        if root is None:
            return 0
        lHeight = height(root.left)
        rHeight = height(root.right)
        return rHeight + 1 if lHeight < rHeight else lHeight + 1

def width(root, level):
    if root is None:
        return 0
    if level == 1:
        return 1
    if level > 1:
        return (width(root.left, level-1) + width(root.right, level-1))

def find_width(root):
    maxWidth = 0
    h = height(root)
    for i in range(1, h+1):
        current_width = width(root, i)
        maxWidth = max(maxWidth, current_width)
    return maxWidth

# lowest common ancestor
def lowest_common_ancestor(root, m, n):
    if root is None or root == m or root == n:
        return root
    left = lowest_common_ancestor(root.left, m, n)
    right = lowest_common_ancestor(root.right, m, n)
    if left is None:
        return right
    elif right is None:
        return left
    else:
        return root
    


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    
    def printLeftView(self, root):
        if root is None:
            return 0
        queue = [root]
        count = 0
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if i == 0:
                    print(node.data)
                    count += 1
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
        return count
    
    def printRightView(self, root):
        if root is None:
            return 0
        queue = [root]
        count = 0
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if i == 0:
                    print(node.data)
                    count += 1
                if node.right != None:
                    queue.append(node.right)
                if node.left != None:
                    queue.append(node.left)
                
        return count
            

n = int(input("No of nodes: "))
nodes = list(map(int, input("Nodes: ").split()))

root = Node(nodes[0]) 

for i in range(1, n):
    root.insert(nodes[i])

# inOrder(root)
# print()
# preOrder(root)
# print()
# postOrder(root)
# print()
# print("Left View")
# print("Height:", root.printLeftView(root))
# print("Right View")
# root.printRightView(root)

# print("Width:", find_width(root))
    
print(lowest_common_ancestor(root, 1, 2))