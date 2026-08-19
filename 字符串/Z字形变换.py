class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if  numRows == 1 or numRows>=len(s):
            return s
    
        dir = 1
        row = 0

        res = ["" for _ in range(numRows)]

        for ch in s:
            res[row] += ch

            if row == 0 :
                dir = 1
            
            if row == numRows -1:
                dir = -1

            row += dir

        return ''.join(res)            
            