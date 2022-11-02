import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lst = []
        for i, node in enumerate(lists):
            if node:
                lst.append((node.val, i, node))
                
        heapq.heapify(lst)
        
        node = ListNode()
        d = node
        while len(lst) > 0:
            val = heapq.heappop(lst)
            
            temp = val[2]
            node.next = temp
            node = node.next
            
            if val[2].next:
                heapq.heappush(lst, (val[2].next.val, val[1], val[2].next))
                
        return d.next

        
        
