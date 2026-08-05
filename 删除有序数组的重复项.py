class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return n,nums

        i = 0
        j = 1
        while j < n:
            while j < n and nums[i] == nums[j]:
                j += 1
            
