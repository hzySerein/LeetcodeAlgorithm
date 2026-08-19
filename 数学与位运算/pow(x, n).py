class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0

        if n < 0:
            n = -n
            x = 1 / x

        res = 1
        base = x
        exp = n

        while exp > 0:
            if exp % 2 != 0:
                res *= base
            base *= base
            exp //= 2

        return res
