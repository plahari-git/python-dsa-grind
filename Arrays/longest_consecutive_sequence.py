class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
            
        nums.sort()
        count = 1
        longest = 1
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                continue
                
            if (nums[i] + 1) == nums[i+1]:
                count += 1
            else:
                count = 1
                
            if count > longest:
                longest = count
                
        return longest
