# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        l=[]
        ans=[]
        if root:
            l.append(root)
        while l:
            s=len(l)
            push=[]
            for i in range(s):
                node=l.pop(0)
                push.append(node.val)
                if node.left:l.append(node.left)
                if node.right:l.append(node.right)
            ans.append(sum(push))
        return ans.index(max(ans))+1