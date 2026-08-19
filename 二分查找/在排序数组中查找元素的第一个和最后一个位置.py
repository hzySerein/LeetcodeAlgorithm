class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def find_first(nums, target):
            """查找第一个等于 target 的索引"""
            left, right = 0, len(nums) - 1
            first = -1
            
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    first = mid
                    right = mid - 1  # 继续向左找更早的
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first
        
        def find_last(nums, target):
            """查找最后一个等于 target 的索引"""
            left, right = 0, len(nums) - 1
            last = -1
            
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    last = mid
                    left = mid + 1  # 继续向右找更晚的
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last
        
        if not nums:
            return [-1, -1]
        
        return [find_first(nums, target), find_last(nums, target)]