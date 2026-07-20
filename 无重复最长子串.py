class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        max_len = 0
        left = 0
        for i in range(len(s)):
            ch = s[i]
            if ch in d and i > left:
                left = d[ch] + 1
            d[ch] = i
            max_len = max(max_len,i - left + 1)

        return max_len

s = Solution()
res = s.lengthOfLongestSubstring("abcabcbb")
print(res)