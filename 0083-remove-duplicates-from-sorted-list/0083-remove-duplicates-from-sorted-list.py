# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        if(head == None):
            return head
        if(head.next ==None):
            return head
        prev = head
        curr = prev.next
        while (curr!= None and prev!=None):
            if(curr.val==prev.val):
                prev.next =curr.next
                curr = curr.next
                continue
            prev=curr
            curr= curr.next
        return head
        