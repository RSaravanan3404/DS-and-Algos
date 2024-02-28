class TreeNode(object):

    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        queue = [ self ]
        while queue:
            node = queue.pop(0)
            if node.left is None:
                node.left = TreeNode(value)
                break
            else:
                queue.append(node.left)

            if node.right is None:
                node.right = TreeNode(value)
                break
            else:
                queue.append(node.right)

            

def create_tree() -> TreeNode:

    n = int(input("No of nodes: "))
    arr = list(map(int, input("Enter the nodes:").split()))
    if n > 0:
        root = TreeNode(arr[0])
        for i in range(1, n):
            root.insert(arr[i])

        return root

    else:
        raise Exception("You must specify atleast one node to create a tree.")
