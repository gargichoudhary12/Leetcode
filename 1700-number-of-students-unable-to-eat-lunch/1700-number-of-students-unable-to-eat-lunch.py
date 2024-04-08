class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s=[]
        j=0
        for i in range(0,len(students)):
            s.append(students[i])

            while len(s)>0 and s[-1]==sandwiches[j]:
                s.pop()
                j=j+1
        
               
        return len(s)

