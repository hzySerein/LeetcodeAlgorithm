class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        n = len(strs)
        if n == 1:
            return strs[0]

        min_len = float('inf')
        for s in strs:
            min_len = min(len(s),min_len)
        
        idx = 0
        res = ''
        while idx < min_len:
            for i in range(1,n):
                if strs[i][idx] != strs[0][idx]:
                    return res
            res += strs[0][idx]
            idx += 1
        return res


            
