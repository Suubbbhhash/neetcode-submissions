from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==1:
            return nums
        count=Counter(nums)
        nums.sort(key=lambda x:(count[x],-x))
        res=[]
        i=len(nums)-1
        count=0
        while i>=0:
            if len(res)==k:
                break
            if nums[i] in res:
                i-=1
            else:
                res.append(nums[i])
                count+=1
                i-=1
        return res

        
    