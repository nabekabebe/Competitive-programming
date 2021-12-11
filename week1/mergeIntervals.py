class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        
        lst = []
        if len(intervals) == 1:
            return intervals
        
        a = intervals[0]
        for i in range(1, len(intervals)):
           
            if a[1] >= intervals[i][0]:
                a = [a[0], intervals[i][1] if (intervals[i][1] > a[1]) else a[1] ]  
                if i == (len(intervals)-1):
                    lst.append(a)
            else:
                if i == (len(intervals)-1):
                    lst.append(intervals[i])
                lst.append(a)
                a = intervals[i]
                
        return lst
