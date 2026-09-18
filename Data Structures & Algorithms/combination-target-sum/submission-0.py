class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        sol=[]
        def dqs(i,cursum):
            if cursum==target:
                res.append(sol[:])
                return
            if cursum>target or i==len(nums):
                return
            dqs(i+1,cursum)
            sol.append(nums[i])
            dqs(i,cursum+nums[i])
            sol.pop()
        dqs(0,0)
        return res