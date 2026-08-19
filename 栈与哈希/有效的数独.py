class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def unique_valid(ls):
            s = set()
            for i in ls:
                if i in s and i != '.':
                    return False
                s.add(i)
            return True

        def matrix_valid(ls):
            s = set()
            for i in range(3):
                for j in range(3):
                    if ls[i][j] in s and ls[i][j] != '.':
                        return False
                    s.add(ls[i][j])
            return True

        for row in board:
            if not unique_valid(row):
                return False
        
        # 检查每一列
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not unique_valid(column):
                return False
        
        # 检查每个 3x3 子矩阵
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_matrix = [
                    [board[i][j], board[i][j+1], board[i][j+2]],
                    [board[i+1][j], board[i+1][j+1], board[i+1][j+2]],
                    [board[i+2][j], board[i+2][j+1], board[i+2][j+2]]
                ]
                if not matrix_valid(sub_matrix):
                    return False
        
        return True

        

