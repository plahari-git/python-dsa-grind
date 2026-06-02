
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        if x>=0:
            n=x
            y=0
            ans=0
            while(x != 0):
                y = x % 10
                x = x // 10
                ans = (ans * 10) + y
            if ans==n:
                return True
            else:
                return False
