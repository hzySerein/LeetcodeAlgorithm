class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
        res = 0
        idx = 0
        n = len(s)
        while idx < n:
            temp = idx + 1
            if temp < n:
                if s[idx] == 'I':
                    if s[temp] == 'V':
                        res += dic['IV']
                        idx += 2
                    elif s[temp] == 'X':
                        res += dic['IX']
                        idx += 2
                    else:
                        res += dic['I']
                        idx += 1
                elif s[idx] == 'X':
                    if s[temp] == 'L':
                        res += dic['XL']
                        idx += 2
                    elif s[temp] == 'C':
                        res += dic['XC']
                        idx += 2
                    else:
                        res += dic['X']
                        idx += 1
                elif s[idx] == 'C':
                    if s[temp] == 'D':
                        res += dic['CD']
                        idx += 2
                    elif s[temp] =='M':
                        res += dic['CM']
                        idx += 2
                    else:
                        res += dic['C']
                        idx += 1
                else:
                    res += dic[s[idx]]
                    idx += 1
            else:
                res += dic[s[idx]]
                idx += 1
        
        return res 
    
    def romanToInt2(self, s):
        dic = {'M':1000, 'CM':900, 'D':500, 'CD':400, 
               'C':100, 'XC':90, 'L':50, 'XL':40, 
               'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
        res = 0
        idx = 0
        n = len(s)
        
        while idx < n:
            if idx + 1 < n:
                two_char = s[idx] + s[idx+1]
                if two_char in dic:  
                    res += dic[two_char]
                    idx += 2
                    continue
            
            res += dic[s[idx]]
            idx += 1
        
        return res

s = Solution()
print(s.romanToInt("III"))