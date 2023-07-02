class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirX = 0
        dirY = 1
        x=0
        y=0
        for d in instructions:
            if d=="G":
                x = x+dirX
                y = y+dirY
            
            
            elif d=="L":
                dirX, dirY = -1*dirY, dirX
                
            else:
                dirX, dirY = dirY, -1*dirX
        return (x,y)==(0,0) or (dirX,dirY)!=(0,1)