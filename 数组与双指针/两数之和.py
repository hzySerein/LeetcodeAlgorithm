class Solution(object):
    def twoSum(self, nums, target):
        d =  dict()
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [i,d[target-nums[i]]]
            d[nums[i]] = i


s = Solution()
result = s.twoSum([2, 7, 11, 15], 9)
print(result)  
