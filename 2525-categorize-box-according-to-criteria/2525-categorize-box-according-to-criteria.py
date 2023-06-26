class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulk , heavy = 0 , 0 
        vol = length*width*height 
        if length >= 10**4 or width >= 10**4 or height >= 10**4  or vol >= 10**9:
            bulk = 1
        if mass >= 100:
            heavy = 1 
        if bulk == 1 and heavy == 1:
            return "Both"
        elif bulk == 0 and heavy == 0 :
            return "Neither"
        elif bulk == 1 and heavy == 0 :
            return "Bulky"
        elif heavy == 1 and bulk == 0 :
            return "Heavy"