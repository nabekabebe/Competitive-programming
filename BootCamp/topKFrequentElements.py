import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values = defaultdict(int)
        for i in nums:
            values[i] += 1
        
        result = []
        for j, l in values.items():
            result.append([-1*l, j])
            
        heapq.heapify(result)

        return [ heapq.heappop(result)[1] for i in range(k)]
