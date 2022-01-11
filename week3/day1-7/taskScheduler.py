class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int: 
        counts = defaultdict(int)
        for i in tasks:
            counts[i] += 1
            
        max_count = max(counts.values())           
    
        result = (max_count-1)*(n+1)
        
        
        for count in counts.values():
            if count == max_count:                
                result += 1
                
        return max(result, len(tasks))
