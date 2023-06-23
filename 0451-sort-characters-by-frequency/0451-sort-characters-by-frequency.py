class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        ans = ""
        for i in sorted(dic.items(), key=lambda x:x[1]):
            ans += i[0] * i[1]
      
        return ans[::-1]