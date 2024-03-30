class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if (not root.left and root.right) or (root.left and not root.right):
            return False

        lq = [ root.left ]
        rq = [ root.right ]

        while lq and rq:
            l = lq.pop(0)
            r = rq.pop(0)
            if l.val != r.val:
                return False
            if l.left and r.right:
                lq.append(l.left)
                rq.append(r.right)
            elif l.left or r.right:
                return False
            if l.right and r.left:
                lq.append(l.right)
                rq.append(r.left)
            elif l.right or r.left:
                return False

        return True
    

