class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0 :
            num = -x
        else:
            num = x
        
        res = 0
        while num > 0:
            a = num % 10
            res = res * 10 + a
            num //= 10
        
        if x < 0:
            res = -res
        
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res
