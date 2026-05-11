class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        res=[]
        j=i+1
        while j<len(nums) and i<len(nums):
            
            if nums[i]+ nums[j]==target:
                return [i,j]
            j+=1
            if j==len(nums):
                i+=1
                j=i+1