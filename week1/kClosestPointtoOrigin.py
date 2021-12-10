class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        lst  = [0] * len(points)
        for i in range(len(points)):
            sqr = math.sqrt((points[i][0])**2 + (points[i][1])**2)
            lst[i] = [sqr, points[i]]
            

        lst.sort(key=lambda x:x[0])
        return [lst[i][1] for i in range(k)]
    
   
