class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i=0
        nums.sort()
        n=len(nums)
        a=False
        if n==1:
            return a
        while i<n:
            if nums[i]==nums[i-1]:
                a=True
            
            i+=1
        return a
            

