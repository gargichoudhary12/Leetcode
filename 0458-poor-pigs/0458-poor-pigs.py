class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return math.ceil(math.log2(buckets)/math.log2(minutesToTest/minutesToDie+1))
        
        
        
        
        
