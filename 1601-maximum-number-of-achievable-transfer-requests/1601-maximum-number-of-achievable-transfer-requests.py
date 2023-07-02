class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        arr = [0] * n
        self.res = 0
        def backtracking(i,n_Request_processed,a):
            if(i == len(requests)):
                if(a == [0] * n):
                    self.res = max(self.res,n_Request_processed)
                return
            From = requests[i][0]
            To = requests[i][1]
            a_move = a[:]
            a_move[From] -= 1
            a_move[To] += 1
            
            backtracking(i+1,n_Request_processed+1,a_move)
           
            backtracking(i+1,n_Request_processed,a[:])
            
        backtracking(0,0,arr)
        return self.res