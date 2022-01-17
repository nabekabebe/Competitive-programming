class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        elif n < 1 or (n % 4 > 0):
            return False
        else:
            return self.isPowerOfFour(n//4)
