class Solution:
    def restoreArray(self,pairs: List[List[int]]) -> List[int]:
        dict=defaultdict(list)
        for i,j in pairs:
            dict[i].append(j)
            dict[j].append(i)
        vis=set()
        ans=[]
        for i in dict:
            if len(dict[i])==1:
                start=i
        self.dfs(dict,ans,vis,start)
        return ans
    def dfs(self,dict,ans,vis,node):
        vis.add(node)
        ans.append(node)
        for j in dict[node]:
            if j not in vis:
                self.dfs(dict,ans,vis,j)
        return