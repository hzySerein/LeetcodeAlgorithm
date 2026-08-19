class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        n = len(nums)
        res = []

        nums.sort()
        i = 0
        for i in range(n-2):
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break
            if nums[i] + nums[n-1] + nums[n-2] < 0:
                continue

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l,r = i + 1,n - 1
            while l < r :
                temp = nums[i] + nums[l] + nums[r]
                if temp == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    while l + 1 < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                    while r - 1 >l and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
                elif temp < 0:
                    l += 1
                else:
                    r -= 1
            
        return res

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))