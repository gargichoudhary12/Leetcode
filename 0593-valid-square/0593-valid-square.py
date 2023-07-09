class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1==p2==p3==p4:
            return False
        def dist(x,y):
            return (x[0]-y[0])**2+(x[1]-y[1])**2
        distance=[dist(p1,p2),dist(p1,p3),dist(p1,p4),dist(p2,p3),dist(p2,p4),dist(p3,p4)]
        distance.sort()
        if distance[0]==distance[1]==distance[2]==distance[3]:
            if distance[4]==distance[5]:
                return True
        return False