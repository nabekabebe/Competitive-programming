# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        start = ListNode(val = 0)
        start.next = head
        end = head
        
        for i in range(1 , n):
            end = end.next
        
        while end.next != None:
            start = start.next
            end = end.next     
            print(start.val, end.val)
        
        if start.next != head:
            start.next = start.next.next
            return head
        else:
            return head.next
