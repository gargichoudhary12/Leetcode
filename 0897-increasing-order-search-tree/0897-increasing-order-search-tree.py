class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy = rtree = TreeNode()
        
        def inorder(node):
            nonlocal rtree
            if node:
                inorder(node.left)
                rtree.right = TreeNode(node.val)
                rtree = rtree.right
                inorder(node.right)
        
        inorder(root)
        
        return dummy.right