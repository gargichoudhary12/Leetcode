class Solution:
    def isPathCrossing(self, path: str) -> bool:
        current_position = [0,0]
        pastpositions = list([[0,0]])
        
        for j in path:
            if j == "N":
                current_position[0] += 1
            if j == "E": 
                current_position[1] += 1  
            if j == "S": 
                current_position[0] -= 1
            if j == "W": 
                current_position[1] -= 1
            
            if list(current_position) in pastpositions:
                return True
            pastpositions.append(list(current_position))