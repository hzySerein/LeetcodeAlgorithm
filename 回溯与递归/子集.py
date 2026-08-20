class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        path = []
        n = len(nums)
        def backtrack(start):
            res.append(path[:])
            for i in range(start,n):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()


        backtrack(0)

        return res