class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set1=set(nums)
        list1=list(set1)
        list1.sort(reverse=True)
        if len(list1)>=3:
            return list1[2]   
        else:
            return list1[0]  
