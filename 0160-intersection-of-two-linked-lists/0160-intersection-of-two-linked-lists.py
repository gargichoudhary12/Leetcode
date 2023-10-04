# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_pointer = headA
        b_pointer = headB
        count  = 0
        while a_pointer!=b_pointer:
            a_pointer = a_pointer.next
            b_pointer = b_pointer.next
            if a_pointer==None:
                count+=1
                if count >1:
                    return None
                a_pointer = headB
            if b_pointer==None:
                b_pointer = headA
           
        return a_pointer