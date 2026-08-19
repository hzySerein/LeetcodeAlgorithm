class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        max_area = 0
        while i < j:
            long = j - i

            height1 = height[i]
            height2 = height[j]

            min_height = min(height1,height2)
            max_area = max(max_area,long * min_height)

            if height1 > height2:
                j -= 1
            else:
                i += 1
            
        return max_area
    

