import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                res[i]=math.prod(nums[1:len(nums)])
            elif i==len(nums)-1:
                res[i]=math.prod(nums[0:len(nums)-1])
            else:
                res[i]=math.prod(nums[0:i])*math.prod(nums[i+1:len(nums)])
        return res