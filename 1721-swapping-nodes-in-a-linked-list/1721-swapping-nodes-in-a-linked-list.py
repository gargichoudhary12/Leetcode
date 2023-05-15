# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        arr = []
        while temp!=None:
            arr.append(temp.val)
            temp =temp.next
        arr[k-1], arr[-k] = arr[-k], arr[k-1]
        temp = head
        count = 0
        while temp != None:
            temp.val = arr[count]
            count+=1
            temp = temp.next
        return head
        