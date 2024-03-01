from binary_tree import TreeNode, create_tree


class Solution:

    def boundaries(self, root: TreeNode) -> list[int]:
        q = [ root ]
        left, right, bottom = [], [], []

        while q:
            n = len(q)
            for i in range(n):
                node = q.pop(0)
                if i == 0:
                    left.append(node.val)
                elif i == n-1:
                    right.append(node.val)
                elif not node.left and not node.right:
                    bottom.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return left + bottom + right[::-1]
    

tree = create_tree()
solution = Solution()
print(solution.boundaries(tree))