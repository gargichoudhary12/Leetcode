# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        hsh = {}
        def get_lev_li(root,level=0):
            if root is None:
                return
            VAl = root.val
            hsh[level] = hsh.get(level, []) + [VAl] 
            get_lev_li(root.left, level + 1)
            get_lev_li(root.right,level + 1)
        def even_lev(i):
            return i%2 == 0
        def inc(val):
            return all(i < j and not even_lev(j) and not even_lev(i) for i, j in zip(val, val[1:]))
        def dec(val):
            return all(i > j and even_lev(j) and even_lev(i) for i, j in zip(val, val[1:]))
        get_lev_li(root)
        scr, ht = 0, 0
        for key, val in hsh.items():
          # for case len == 1
            if len(val) == 1:
                if even_lev(key):
                    if even_lev(val[0]):
                        return False
                    else:
                        scr += 1
                elif not even_lev(key):
                    if not even_lev(val[0]):
                        return False
                    else:
                        scr +=1 
            elif even_lev(key):
                if inc(val):
                    scr += 1
            else:
                if dec(val):
                    scr += 1
            ht += 1
        return scr == ht