# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        l1=temp
        if(head==None):
            return
        if(l1.next!=None):
            l2=l1.next
        else:
            return head
        while l1!=None and l2!=None:
            l1.val,l2.val=l2.val,l1.val
            if(l2.next!=None):
                l1=l2.next
            else:
                break
            if(l1.next!=None):
                l2=l1.next
            else:
                break
        return head
        