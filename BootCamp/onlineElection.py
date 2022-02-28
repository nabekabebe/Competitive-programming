class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self. result = self.counting()
        
        
    def q(self, t: int) -> int:
        left, right, best = 0, len(self.times) -1,  0
        
        while left <= right:
            mid = left + (right-left)//2

            
            if self.times[mid] > t:
                right = mid -1
                
            else:
                left = mid + 1 
                best = mid
                
        return self.result[self.times[best]]

    def counting(self):
        count = defaultdict(lambda: -1)
        vote_count = defaultdict(int)
        
        
        cur_max, cur_win = 0, -1
        for p, t in zip(self.persons, self.times):
            vote_count[p] += 1
            if vote_count[p] >= cur_max:
                cur_max, cur_win = vote_count[p], p
                
            count[t] = cur_win
            
        return count
                

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)''
