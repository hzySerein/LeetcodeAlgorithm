class Solution(object):
    def canJump(self, nums):
        maxreach = 0
        i = 0
        n = len(nums)
        while i <= maxreach and i < n:
            maxreach = max(maxreach, i + nums[i])
            if maxreach >= n - 1:
                return True
            i += 1
        return False