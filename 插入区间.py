class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(intervals)
        if n == 0:
            return [newInterval]
        ls = intervals[::]
        ls.append(newInterval)
        ls.sort(key = lambda x:x[0])
        res = []
        j = 0
        res.append(ls[0])
        for i in range(1,n):
            if intervals[i][0] <= res[j][1]:
                res[j][1] = max(ls[i][1],res[j][1])
            else:
                res.append(ls[i])
                j += 1

        return res


s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))