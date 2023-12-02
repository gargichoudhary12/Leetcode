class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        initial_list = list(range(1, n + 1))
        n = len(initial_list)        
        index_value = 0
        while n > 1:
            index_value = (index_value + k - 1) % n
            initial_list.pop(index_value)
            n -= 1
        return initial_list[0]