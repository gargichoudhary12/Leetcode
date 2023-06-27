class Solution:
    def minMaxDifference(self, num: int) -> int:
        
        minimum = num
        maximum = num
        num = str(num)
        for i in num:
            if i<'9':
                maximum = int(num.replace(i,'9'))
                break
        for i in num:
            if i!='0':
                minimum = int(num.replace(i,'0'))
                break
                    
        return (maximum-minimum)