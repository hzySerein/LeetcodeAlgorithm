class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0
        

        row = len(obstacleGrid)
        column = len(obstacleGrid[0])

        if obstacleGrid[row-1][column-1] == 1:
            return 0


        dp = [[0]*(column+1) for _ in range(row+1)]

        dp[0][1] = 1

        for i in range(1,row+1):
            for j in range(1,column+1):
                if obstacleGrid[i-1][j-1] == 1:
                    continue
                dp[i][j] =  dp[i-1][j] + dp[i][j-1]
        return dp[row][column]