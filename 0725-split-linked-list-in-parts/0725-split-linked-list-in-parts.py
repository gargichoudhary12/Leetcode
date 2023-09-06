# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n=0
        p=head
        res=[None]*k
        
        if not head:
            return res

        while p:
            n+=1
            p=p.next
        
        if k>=n and n>0:
            p=head
            i=0
            while p:
                temp=p.next
                p.next=None
                res[i]=p
                i+=1
                p=temp
        else:
            size=n//k
            extra=n%k
            p=head
            prev=p
            curSize=1
            i=0

            while p:
                if curSize==size:
                    if extra!=0:
                        p=p.next
                        extra-=1

                    temp=p.next
                    p.next=None
                    res[i]=prev
                    i+=1
                    p=temp
                    prev=p
                    curSize=1
                else:
                    p=p.next
                    curSize+=1

        return res