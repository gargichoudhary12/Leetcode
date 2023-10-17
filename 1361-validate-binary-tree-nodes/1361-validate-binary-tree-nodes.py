class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        starts = set([i for i in range(n)])
        dic = {}
        for i in range(len(leftChild)):
            if leftChild[i] > -1:
                if i == leftChild[i]:
                    return False
                if leftChild[i] in starts:
                    starts.remove(leftChild[i])
                else:
                    return False
            if rightChild[i] > -1:
                if i == rightChild[i]:
                    return False
                if rightChild[i] in starts:
                    starts.remove(rightChild[i])
                else:
                    return False
            dic[i] = [leftChild[i], rightChild[i]]
        if len(starts) != 1:
            return False
        visited = set()
        def traverse(root):
            if root == -1:
                return True
            if root in visited:
                return False
            visited.add(root)
            return traverse(dic[root][0]) and traverse(dic[root][1])
        return traverse(starts.pop()) and len(visited) == n