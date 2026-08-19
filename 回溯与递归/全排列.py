class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        used = [False] * n
        temp = []
        res = []
        def backtrack():
            if len(temp) == n:
                res.append(temp[:])
                return

            for i in range(n):
                if used[i]:
                    continue
                used[i] = True
                temp.append(nums[i])
                backtrack()
                used[i] = False
                temp.pop()
            
        backtrack()
        return res