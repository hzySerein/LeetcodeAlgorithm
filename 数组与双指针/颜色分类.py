class Solution:
    def sortColors(self, nums):
        n = len(nums)
        if n == 1:
            return nums
        # 初始化三个指针
        left, i, right = 0, 0, n - 1

        while i <= right:
            if nums[i] == 0:
             
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 2:
    
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
              
            else: 

                i += 1