class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        start , max_len = 0 , 0
        def expand_around_center(left,right):
            while left >= 0 and right <len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return left + 1,right - left - 1
        
        for i in range(len(s)):
            l1 ,max1 = expand_around_center(i,i)
            l2 ,max2 = expand_around_center(i,i+1)

            if max1 > max_len:
                start = l1
                max_len = max1

            if max2 > max_len:
                start = l2
                max_len = max2
        
        return s[start:max_len+start]
    

