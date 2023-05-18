import math
import numpy as np
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes=set(np.arange(n))
        for i,j in edges:
            if(j in nodes):
                nodes.remove(j)
        return (nodes)