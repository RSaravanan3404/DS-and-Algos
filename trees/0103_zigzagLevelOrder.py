import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

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
    

