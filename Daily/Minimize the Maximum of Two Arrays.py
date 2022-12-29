class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        left, right, G = 0, 10**10, lcm(divisor1, divisor2)

        while left < right:
            mid = (left+right)//2               
            
            x = mid - mid//divisor1 >= uniqueCnt1        
            y = mid - mid//divisor2 >= uniqueCnt2         
            z = mid - mid//G  >= uniqueCnt1 + uniqueCnt2
            if x and y and z: 
                right = mid 
            else: 
                left = mid+1 

        return left
