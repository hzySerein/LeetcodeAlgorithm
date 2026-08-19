class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        l1 = len(a)
        l2 = len(b)
        i = l1 - 1
        j = l2 - 1
        carry = 0

        while i >=0 or j >= 0 or carry :
            num1 = int(a[i]) if i >= 0 else 0
            num2 = int(b[j]) if j >= 0 else 0

            temp = num1 + num2 + carry
            res = str(temp % 2) + res
            carry = temp // 2

            i -= 1
            j -= 1 
        return res
