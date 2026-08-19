class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        def revserse(x):
            res = 0
            while x > 0:
                a = x % 10
                res = res * 10 + a
                x //= 10
            
            return res
        
        revsere_num = revserse(x)
        
        return x == revsere_num