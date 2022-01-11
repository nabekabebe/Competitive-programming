class Solution:
    def myPow(self, x: float, n: int) -> float:  
        if n == 0:
            return 1
        elif n < 0:
            return self.myPow(1/x, abs(n))

        val = self.myPow(x, n//2)
        if n % 2 == 0:
            return val * val
        else:
            return val * val * x
