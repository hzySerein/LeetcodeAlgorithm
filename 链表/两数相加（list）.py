class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        len1 = len(l1)
        len2 = len(l2)


        if len1 > len2:
            for _ in range(len1-len2):
                l2.append(0)

        else:
            for _ in range(len2-len1):
                l1.append(0)
        
        carry = 0
        ls = []
        for i in range(max(len1,len2)):
            temp = l1[i] + l2[i] + carry
            two_sum = temp%10
            carry = temp//10
            ls.append(two_sum)
        
        if carry:
            ls.append(1)
        return ls
            

s = Solution()
res = s.addTwoNumbers([5,4,3],[5,6,4])
print(res)