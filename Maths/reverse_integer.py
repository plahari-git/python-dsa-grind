class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative = x < 0 
        x = abs(x)
        
        ans = 0
        y = 0
        while(x != 0):
            y = x % 10
            x = x // 10
            ans = (ans * 10) + y
            
        if not is_negative:
            final_ans = ans
        else:
            final_ans = -ans
            
        if final_ans < -2**31 or final_ans > 2**31 - 1:
            return 0
            
        return final_ans
