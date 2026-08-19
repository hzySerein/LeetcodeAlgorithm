class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        n = len(strs)
        if n == 1:
            return [strs] 
        dic = {}
        for i in range(n):
            sort_s = ''.join(sorted(strs[i]))
            if sort_s in dic:
                dic[sort_s].append(strs[i])
            else:
                dic[sort_s] = [strs[i]]

        return list(dic.values()) 

