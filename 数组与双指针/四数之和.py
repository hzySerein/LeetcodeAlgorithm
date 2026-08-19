class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n-3):

            if nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target:
                return res
            
            if i>0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1,n-2):

                if nums[i] + nums[j] + nums[n-2] + nums[n-1] <target:
                    continue

                if j>0 and nums[j] == nums[j-1] and j-1>i:
                    continue

                l = j + 1
                r = n - 1
                two_target = target - nums[i] - nums[j]
                
                while l<r:
                    two_sum = nums[l] + nums[r]
                    if two_sum == two_target:
                        res.append([nums[i],nums[j],nums[l],nums[r]])

                        while l+1<r and nums[l] == nums[l+1]:
                            l+=1
                        l+=1

                        while l<r-1 and nums[r] == nums[r-1]:
                            r-=1
                        r-=1
                    elif two_sum > two_target:
                        r-=1
                    else:
                        l+=1
        return res
    
if __name__=='__main__':
    
    s = Solution()
    ls = [2,2,2,2,2]
    target = 8
    res = s.fourSum(ls,target)
    print(res)
        