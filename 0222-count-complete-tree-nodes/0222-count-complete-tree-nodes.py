# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def count_subtree(node):
            if node is None:
                return 0
            return count_subtree(node.left) + count_subtree(node.right) + 1
        
        return count_subtree(root)