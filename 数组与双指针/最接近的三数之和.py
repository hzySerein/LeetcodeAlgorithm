class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        min_dis = float('inf')
        res = 0
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            l = i + 1
            r = n -1
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                diff = target - temp

                if abs(diff) < min_dis:
                    min_dis = abs(diff)
                    res = temp

                if diff == 0:
                     return res

                elif diff > 0 :
                        l += 1
                else:
                        r -= 1

        return res
                

            