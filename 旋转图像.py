class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l1 = len(matrix[0])
        for i in range(1,l1):
            for j in range(i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        l2 = l1 // 2
        
        for i in range(l1):
            for j in range(l2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][l1 - j - 1]
                matrix[i][l1 - j - 1] = temp

