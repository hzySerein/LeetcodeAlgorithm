class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        end = digits[-1] + 1
        if end < 10 :
            digits[-1] = end
            return digits
        digits[-1] = 0
        idx = len(digits) - 2
        carry = 1
        while idx >= 0:
            if carry == 0:
                return digits
            num = digits[idx] + carry
            if num == 10:
                digits[idx] = 0
                idx -= 1
            else:
                digits[idx] = num 
                carry = 0
                idx -= 1
                 
        if carry == 0:
            return digits
        
        return [1] + digits
    

s = Solution()
print(s.plusOne([9,9]))


'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
'''