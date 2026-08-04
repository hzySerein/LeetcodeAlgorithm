class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res = []

        def helper(l,r,item,res):
            if l > r :
                return
            if l == 0 and r == 0:
                res.append(item)
            if l > 0:
                helper(l-1,r,item+'(',res)
            if r > 0:
                helper(l,r-1,item+')',res)

        helper(n,n,'',res)
        return res


        