class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol=[0]*len(nums)
        n=len(nums)
        for j in range (n):
            res=1
            for i in range (n):
                if i!=j:
                    res*=nums[i]
                
            sol[j]=res
        return sol
            


        