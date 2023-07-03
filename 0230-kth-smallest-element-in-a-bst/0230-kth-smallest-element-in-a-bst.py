# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def inorder(root):
            if not root:
                return []
            l=inorder(root.left)
            r=inorder(root.right)
            return l+[root.val]+r
        arr=inorder(root)
        print(arr)
        return arr[k-1]
     
        