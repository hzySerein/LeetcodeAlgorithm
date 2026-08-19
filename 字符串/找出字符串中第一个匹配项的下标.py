class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l1 = len(haystack)

        l2 = len(needle)

        for i in range(l1-l2+1):
            if haystack[i:i+l2] == needle:
                return i
        return -1
    

