# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.visited = []
        

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        visit_order1 = []
        order1 = self.dfs(root1, visit_order1)
        visit_order2 = []
        order2 = self.dfs(root2, visit_order2)
        return order1 == order2
        
        
    def dfs(self, TreeNode, visit_order):
        self.visited.append(TreeNode)
        if TreeNode.left == None and TreeNode.right == None:
            visit_order.append(TreeNode.val)
        else:
            for w in [TreeNode.left, TreeNode.right]:
                if w != None:
                    if w not in self.visited:
                        self.dfs(w, visit_order)
        return visit_order