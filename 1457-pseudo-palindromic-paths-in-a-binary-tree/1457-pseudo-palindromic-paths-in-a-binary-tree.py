# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def ppp(node, l):
            if node.left == node.right == None:
                tmp = l.copy()
                tmp[node.val - 1] += 1
                odds = 0
                for i in tmp:
                    if i % 2 == 1:
                        odds += 1
                if odds >= 2:
                    return 0
                return 1
            tmp = l.copy()
            tmp[node.val - 1] += 1
            if node.left != None and node.right != None:
                return ppp(node.left, tmp) + ppp(node.right, tmp)
            if node.left != None:
                return ppp(node.left, tmp)
            return ppp(node.right, tmp)
        return ppp(root, [0 for i in range(9)])