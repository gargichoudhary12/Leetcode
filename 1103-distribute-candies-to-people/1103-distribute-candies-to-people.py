class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0]*num_people
        count = 0
        while candies>0:
            for i in range(len(res)):
                count+=1
                if candies>=count:
                    res[i]+=count
                else:
                    res[i]+=candies
                    return res
                candies-=count
        return res
                
                
                
                
                
                
                
                
                
                