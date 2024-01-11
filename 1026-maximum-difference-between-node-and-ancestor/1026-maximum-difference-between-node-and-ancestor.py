# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        mini, maxi = root.val, root.val
        ans = 0
        st = [(root, mini, maxi)]
        while st:
            node, a, b = st.pop()
            if node.right:
                mini = min(node.right.val, node.val, a)
                maxi = max(node.right.val, node.val, b)
                ans = max(ans, maxi-mini)
                st.append((node.right,mini , maxi))
            if node.left:
                mini = min(node.left.val, node.val, a)
                maxi = max(node.left.val, node.val, b)
                ans = max(ans, maxi-mini)
                st.append((node.left,mini , maxi))
        return ans
