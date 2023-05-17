# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        maximumSum = 0
        string = []
        
        while curr:
            string.append(curr.val)
            curr = curr.next
            
        
        curr = head
        length = len(string)
        count = 0
        maximumSum = 0
        while (count<=length/2):
            maximumSum = max(maximumSum, curr.val+string.pop())
            curr = curr.next
            count+=1
        return maximumSum