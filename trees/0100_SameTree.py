from trees.binarytree import TreeNode, create_tree

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        q1 = [ p ]
        q2 = [ q ]
        while q1 and q2:
            node1 = q1.pop(0)
            node2 = q2.pop(0)
            if node1.val != node2.val:
                return False
            if node1.left and node2.left:
                q1.append(node1.left)
                q2.append(node2.left)
            elif node1.left or node2.left:
                return False
            if node1.right and node2.right:
                q1.append(node1.right)
                q2.append(node2.right)
            elif node1.right or node2.right:
                return False

        return True
    

tree1 = create_tree()
tree2 = create_tree()
solution = Solution()
print(solution.isSameTree(tree1, tree2))