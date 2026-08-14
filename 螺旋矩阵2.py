class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return [[1]] 
        l = n**2
        res = [[0]*n for _ in range(n)]

        top,bottom = 0,n-1
        left,right = 0,n-1

  
        num = 1

        while top <= bottom and left <= right:
            res[top][left:right+1] = range(num,num + (right - left + 1))
            top += 1
            num += right - left + 1

            for i in range(top,bottom + 1):
                res[i][right] = num
                num +=1
            right -= 1

            if top <= bottom:
                res[bottom][left:right+1] = range(num,num+right-left+1)[::-1]
                bottom -= 1
                num += right - left + 1

            if left <= right:
                for i in range(bottom,top-1,-1):
                    res[i][left] = num
                    num += 1
                left += 1
        
        return res
