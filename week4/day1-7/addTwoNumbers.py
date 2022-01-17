# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        
        
        head.val = (l1.val + l2.val) % 10
        carry = (l1.val + l2.val) // 10
        
        
        l1, l2 = l1.next, l2.next
        temp = head
        while (l1 != None or l2 != None) or carry > 0:
            new = ListNode()
            if l1 != None:
                new.val += l1.val
                l1 = l1.next
            if l2 != None:
                new.val += l2.val
                l2 = l2.next
                
            new.val += carry
            carry = (new.val) // 10
            new.val = new.val % 10
            
            temp.next = new
            temp = new
            
        temp.next = None
        return head
        
