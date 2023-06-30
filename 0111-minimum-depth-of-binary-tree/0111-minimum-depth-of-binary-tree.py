# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def mindepth(root):
            if root is None:
                return 0
            if root.left is None:
                return 1+ mindepth(root.right)
            if root.right is None:
                return 1+mindepth(root.left)
            return 1+min(self.minDepth(root.left),self.minDepth(root.right))
        
        return mindepth(root)