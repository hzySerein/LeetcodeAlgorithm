class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res = ['']

        n = len(digits)

        for num in digits:
            temp = []
            for ch in dic[num]:
                for str in res:
                    temp.append(str+ch)
            res = temp
            
        return res

