class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            elif prices[i] - min > profit:
                profit = prices[i] - min
        return profit