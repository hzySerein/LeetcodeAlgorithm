class Solution(object):
    def mySqrt(self, x):
        if x <= 1:
            return x
        
        l, r = 1, x // 2 
        
        while l <= r:
            mid = (l + r) // 2
            square = mid * mid
            
            if square == x:
                return mid
            elif square < x:
                l = mid + 1
            else:
                r = mid - 1
        
        return r