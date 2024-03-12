# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a= []
        stack = []
        ptr = head
        while ptr:
            a.append(ptr.val)
            ptr = ptr.next
        for e in a:
            if e == 0:
                continue
            tot = 0
            temp = []
            flag = False
            while stack:
                v = stack.pop()
                tot+=v
                temp.append(v)
                if tot == -e:
                    flag = True
                    break
            if flag:
                continue
            else:
                while temp:
                    v = temp.pop()
                    stack.append(v)
            stack.append(e)
        
        head = ListNode()
        l = head
        for e in stack:
            l.next = ListNode()
            l = l.next
            l.val = e
            
        return head.next