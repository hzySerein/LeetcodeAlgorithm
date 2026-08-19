class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        column = len(matrix[0])

        first_row_has_zero = any(matrix[0][j] == 0 for j in range(column))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(row))

        for i in range(1,row):
            for j in range(1,column):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, row):
            for j in range(1, column):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0  
        if first_row_has_zero:
            for j in range(column):
                matrix[0][j] = 0
        
        # 处理第一列
        if first_col_has_zero:
            for i in range(row):
                matrix[i][0] = 0