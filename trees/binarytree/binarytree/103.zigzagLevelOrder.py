import collections
from binary_tree import TreeNode, create_tree

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        res = []
        if not root:
            return res
        flip = -1
        q = collections.deque( [root] )
        while q:
            lvl = []
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                lvl.append(node.val)
            flip *= -1
            res.append(lvl[::flip])

        return res
    

tree = create_tree()
solution = Solution()
[print(level) for level in solution.zigzagLevelOrder(tree)]