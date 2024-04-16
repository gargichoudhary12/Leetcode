# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # new root
        if depth == 1:
            return TreeNode(val, left = root)

        queue = [(root, 1)]     # stores (node, layer)

        while queue:
            curr, d = queue.pop(0)

            # children of curr should go one layer below
            if d == depth - 1 :
                # create left and right nodes
                left_node = TreeNode(val)
                right_node = TreeNode(val)

                # update pointers for the children of curr
                left_node.left = curr.left
                right_node.right = curr.right

                # curr node should point to th new created nodes
                curr.left = left_node
                curr.right = right_node
                
            # add left subtree
            if curr.left:
                queue += [(curr.left, d + 1)]

            # add right subtree
            if curr.right:
                queue += [(curr.right, d + 1)]

        return root