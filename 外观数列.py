class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
            
        s = self.countAndSay(n-1)
        l = len(s)
        res = ''
        i = 0
        while i < l:
            ch = s[i]
            j = i + 1
            while j < l and s[j] == ch:
                j += 1
            res += str(j-i) + ch
            i = j 
        return res  

