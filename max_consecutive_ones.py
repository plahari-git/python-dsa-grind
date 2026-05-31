class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        max_streak=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                if count>max_streak:
                    max_streak=count
            else:
                count=0
        return max_streak
