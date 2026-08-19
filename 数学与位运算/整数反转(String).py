class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s1 = str(x)
        n = len(s1)
        
        if x < 0:
            s2 = s1[:0:-1]  
            s2 = '-' + s2
        else:
            s2 = s1[::-1]
        
        res = int(s2)
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res

# 测试
s = Solution()
print(s.reverse(123))    
print(s.reverse(-123))   
print(s.reverse(120))    