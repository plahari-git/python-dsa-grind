class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        n=len(nums)
        set1=set(nums)
        for i in range(1,n+1):
            if i not in set1:
                res.append(i)
        return res