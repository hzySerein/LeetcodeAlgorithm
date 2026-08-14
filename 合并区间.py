class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(intervals)
        if n == 1:
            return intervals

        intervals.sort(key = lambda x:x[0])
        res = []
        j = 0
        res.append(intervals[0])
        for i in range(1,n):
            if intervals[i][0] <= res[j][1]:
                res[j][1] = max(intervals[i][1],res[j][1])
            else:
                res.append(intervals[i])
                j += 1

        return res


s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))