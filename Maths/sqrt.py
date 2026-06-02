class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            square = mid * mid
            
            if square == x:
                return mid
            elif square > x:
                high = mid - 1
            else:
                ans = mid
                low = mid + 1
                
        return ans
