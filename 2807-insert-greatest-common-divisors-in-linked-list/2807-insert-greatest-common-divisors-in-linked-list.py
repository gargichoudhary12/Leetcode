# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        
        while curr and curr.next:
            a = curr.val
            b = curr.next.val
            d = gcd(a, b)
            
            temp = curr.next
            curr.next = ListNode(d, curr.next)
            curr = temp

        return head