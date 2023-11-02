# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        def dfs(root):
            if root == None:
                return [0,0]
            l,cl = dfs(root.left)
            r,cr = dfs(root.right)
            if (root.val + l + r) // (cl + cr + 1) == root.val:
                self.count += 1
            return [root.val + l + r, cl + cr + 1] 
        dfs(root)
        return self.count