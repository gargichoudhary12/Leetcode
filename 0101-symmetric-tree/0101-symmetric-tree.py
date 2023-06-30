# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def ismirror(root1, root2):
            if root1 is None and root2 is None:
                return True
            if (root1 is not None and root2 is not None):
                if root1.val == root2.val:
                    return (ismirror(root1.left, root2.right) and ismirror(root1.right, root2.left))
            return False
        return ismirror(root,root)