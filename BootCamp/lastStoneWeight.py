class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        lst = [i*-1 for i in stones]
        heapq.heapify(lst)
        
        
        while len(lst) > 1:
            first = (-1*heapq.heappop(lst))
            second = -1*(heapq.heappop(lst))
            
            if first > second:
                result  = first - second
                heapq.heappush(lst, -1*result)
                
            
        return -1*lst[0] if len(lst) > 0 else 0
