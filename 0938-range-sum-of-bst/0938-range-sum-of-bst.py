# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = [0]
        self.helper(root,low,high,total)
        return total[0]
    
    def helper(self,root, low, high, total):
        if not root:
            return
        if low<=root.val<=high:
            total[0]+=root.val
        self.helper(root.left, low, high, total)
        self.helper(root.right, low, high, total)
