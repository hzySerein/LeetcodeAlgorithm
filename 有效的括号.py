class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n % 2 != 0:
            return False

        stack = []
        dic = {'(':')','{':'}','[':']'}
        for i in s:
            if i in dic:
                stack.append(i)
            else:
                top = stack.pop()
                if dic[top] != i:
                    return False
        if stack:
            return False
        return True

s = Solution()
print(s.isValid('[]'))